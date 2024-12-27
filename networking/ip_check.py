# tools/networking/ip_check.py

import socket

def run():
    hostname = input("Enter hostname (e.g., google.com): ")
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address of {hostname} is {ip_address}")
    except socket.gaierror:
        print("Error: Invalid hostname")
