# WireGuard ISP Checker

This Python script retrieves information about WireGuard connections, specifically the allowed IPs and endpoint IP addresses, and then uses the IP addresses to fetch the ISP information using the ipinfo.io API.

## Prerequisites

- Python 3.x
- Requests library (install using `pip install requests`)

## Usage

1. Ensure you have the necessary prerequisites installed.

2. If you encounter the error "Error: Command '['wg', 'show']' returned non-zero exit status 1," you may need to run the script with elevated privileges. Use the following command:

   ```bash
   sudo python wireguard_isp_checker.py
   ```

   Make sure you have the necessary permissions to run `sudo` commands.

3. Optionally, if you want the script to refresh automatically, you can use the `watch` command before executing the script:

   ```bash
   watch -n 1 sudo python wireguard_isp_checker.py
   ```

   This will run the script every second, refreshing the information automatically.

## Configuration

You can customize the script by modifying the following variables in the script:

- `IPINFO_API_URL`: The URL for the ipinfo.io API. You can change this if needed.
- `INTERNAL_IP_PREFIX`: The prefix used to identify internal IP addresses.
