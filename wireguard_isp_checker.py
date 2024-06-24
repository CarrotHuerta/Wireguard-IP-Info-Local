import re
import requests
from colorama import Fore, Style
from datetime import datetime, timedelta
import os
import subprocess
import csv

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')

# clear screen
clear_screen()

def init_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ip', 'isp'])

def get_isp_from_csv(ip, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ip'] == ip:
                return row['isp']
    return None

def save_isp_to_csv(ip, isp, file_path):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip, isp])

def get_isp(ip, file_path):
    if ip.startswith("10.20"):
        return "INTERNAL"
    
    isp = get_isp_from_csv(ip, file_path)
    if isp:
        return isp
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        isp = data.get('org', 'Unknown ISP')
        save_isp_to_csv(ip, isp, file_path)
        return isp
    except:
        return "Unknown ISP"

def is_online(last_handshake):
    last_handshake = last_handshake.split(', ')
    hours, minutes, seconds = 0, 0, 0

    for part in last_handshake:
        if 'hour' in part:
            hours = int(part.split()[0])
        elif 'minute' in part:
            minutes = int(part.split()[0])
        elif 'second' in part:
            seconds = int(part.split()[0])

    total_minutes = hours * 60 + minutes + seconds / 60
    return total_minutes <= 2

def main():
    csv_file_path = 'isp_data.csv'
    init_csv(csv_file_path)

    try:
        # run `wg show` command locally
        output = subprocess.check_output(['wg', 'show'], universal_newlines=True)

        allowed_ips_info = re.findall(r'allowed ips: ([\d.]+/\d+)', output)
        endpoint_info = re.findall(r'endpoint: ([\d.]+):', output)
        handshake_info = re.findall(r'latest handshake: (.+)', output)

        ip_isp_info = []
        for allowed_ips, endpoint_ip, last_handshake in zip(allowed_ips_info, endpoint_info, handshake_info):
            isp = get_isp(endpoint_ip, csv_file_path)
            online_status = is_online(last_handshake)
            ip_isp_info.append((allowed_ips.split('/')[0], endpoint_ip, isp, online_status))

        sorted_ip_isp_info = sorted(ip_isp_info, key=lambda x: [int(i) for i in x[0].split('.')])

        for ip, endpoint_ip, isp, online_status in sorted_ip_isp_info:
            if online_status:
                print(f"IP: {ip}, Endpoint: {endpoint_ip}, ISP: {isp}, Status: {Fore.GREEN}Online{Style.RESET_ALL}")
            else:
                print(f"IP: {ip}, Endpoint: {endpoint_ip}, ISP: {isp}, Status: {Fore.RED}Offline{Style.RESET_ALL}")

    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()
