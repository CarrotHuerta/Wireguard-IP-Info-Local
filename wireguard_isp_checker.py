import re
import subprocess
import requests

def get_isp(ip):
    if ip.startswith("10.20"):
        return "INTERNAL"
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        isp = data.get('org', 'Unknown ISP')
        return isp
    except:
        return "Unknown ISP"

def main():
    try:
        # Run the 'wg show' command locally
        result = subprocess.run(['wg', 'show'], capture_output=True, text=True, check=True)
        output = result.stdout

        allowed_ips_info = re.findall(r'allowed ips: ([\d.]+/\d+)', output)
        endpoint_info = re.findall(r'endpoint: ([\d.]+):', output)

        for allowed_ips, endpoint_ip in zip(allowed_ips_info, endpoint_info):
            isp = get_isp(endpoint_ip)
            print(f"IP: {allowed_ips.split('/')[0]}, Endpoint: {endpoint_ip}, ISP: {isp}")

    except subprocess.CalledProcessError as e:
        print("Error:", str(e))
    except requests.RequestException as e:
        print("Error fetching ISP information:", str(e))

if __name__ == '__main__':
    main()
