import socket
import requests
import subprocess
import argparse
from datetime import datetime

# Colors for Linux terminal
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"

def track_ip(ip):
    """Tracks IP information using an API."""
    print(f"{CYAN}Tracking IP: {ip}{RESET}")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print(f"{RED}Failed to fetch IP details.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def lookup_website_history(domain):
    """Searches for website history using Wayback Machine."""
    print(f"{CYAN}Looking up history for: {domain}{RESET}")
    try:
        response = requests.get(f"http://web.archive.org/cdx/search/cdx?url={domain}&output=json")
        if response.status_code == 200:
            entries = response.json()[1:]
            print(f"{GREEN}Found {len(entries)} historical snapshots:{RESET}")
            for entry in entries[:5]:
                print(f"- {entry[1]} on {entry[2]}")
        else:
            print(f"{RED}No historical data found for {domain}.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def port_scan(target, ports):
    """Performs a basic port scan on the target."""
    print(f"{CYAN}Scanning ports on: {target}{RESET}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{GREEN}Port {port} is open.{RESET}")
            sock.close()
        except Exception as e:
            print(f"{RED}Error scanning port {port}: {e}{RESET}")

def run_ping(target):
    """Runs a ping command to check if the target is reachable."""
    print(f"{CYAN}Pinging: {target}{RESET}")
    try:
        result = subprocess.run(["ping", "-c", "4", target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"{RED}Error running ping: {e}{RESET}")

def menu():
    while True:
        print(f"\n{CYAN}Multi-Function Networking Tool{RESET}")
        print("1. Track IP")
        print("2. Lookup Website History")
        print("3. Scan Ports")
        print("4. Ping a Target")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            ip = input("Enter the IP address: ")
            track_ip(ip)
        elif choice == "2":
            domain = input("Enter the domain name: ")
            lookup_website_history(domain)
        elif choice == "3":
            target = input("Enter the target: ")
            ports = input("Enter ports to scan (comma-separated, e.g., 22,80,443): ")
            port_list = [int(port.strip()) for port in ports.split(",")]
            port_scan(target, port_list)
        elif choice == "4":
            target = input("Enter the target to ping: ")
            run_ping(target)
        elif choice == "5":
            print(f"{GREEN}Exiting the tool. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    menu()
