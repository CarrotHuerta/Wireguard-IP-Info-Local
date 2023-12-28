# WireGuard ISP Checker

This Python script retrieves information about WireGuard connections, specifically the allowed IPs and endpoint IP addresses, and then uses the IP addresses to fetch the ISP information using the ipinfo.io API.

## Prerequisites

- Python 3.x
- Requests library (install using `pip install requests`)

## Usage

1. Ensure you have the necessary prerequisites installed.

2. Run the script:

   ```bash
   python local.py
   ```

   This will execute the script, fetch the WireGuard connection information, and print details including the allowed IPs, endpoint IPs, and ISP information.

## Configuration

You can customize the script by modifying the following variables in the script:

- `IPINFO_API_URL`: The URL for the ipinfo.io API. You can change this if needed.
- `INTERNAL_IP_PREFIX`: The prefix used to identify internal IP addresses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
