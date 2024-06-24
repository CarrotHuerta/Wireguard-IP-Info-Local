# WireGuard ISP Checker

This Python script retrieves information about WireGuard connections, specifically the allowed IPs and endpoint IP addresses, and then uses these IP addresses to fetch the ISP information using the ipinfo.io API. It also checks if the WireGuard connections are currently online based on the last handshake time.

## Prerequisites

- Python 3.x
- Requests library (install using `pip install requests`)
- Colorama library (install using `pip install colorama`)

## Usage

1. Ensure you have the necessary prerequisites installed:
   ```bash
   pip install requests colorama
   ```

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
- `csv_file_path`: The file path for the CSV file used to store ISP data.
- `IPINFO_API_URL`: The URL for the ipinfo.io API. You can change this if needed.
- `INTERNAL_IP_PREFIX`: The prefix used to identify internal IP addresses (currently set to `10.20`).

## Script Details

The script performs the following steps:
1. Clears the terminal screen for better readability.
2. Initializes a CSV file to store ISP information if it doesn't already exist.
3. Runs the `wg show` command to get information about WireGuard connections.
4. Extracts the allowed IPs, endpoint IPs, and latest handshake times from the command output using regular expressions.
5. For each endpoint IP, retrieves the ISP information from ipinfo.io or the CSV file if it was previously stored.
6. Determines if the connection is online based on the last handshake time.
7. Prints the IP, endpoint IP, ISP, and online status in a sorted and color-coded format.

## Error Handling

The script includes basic error handling to catch and print exceptions that may occur during execution. Ensure you have the necessary permissions and dependencies installed to avoid common issues.
