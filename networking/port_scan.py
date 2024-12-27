# tools/networking/port_scan.py

import socket

def run():
    host = input("Enter host to scan (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    print(f"Scanning ports on {host} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is open")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
