import ipaddress
import socket
from ipwhois import IPWhois

def run(ip):
    try:
        # Validate IP address format
        print(f"Validating IP: {ip}")
        ipaddress.ip_address(ip)
        print(f"Scanning IP: {ip}")
        
        # Get reverse DNS information
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            print(f"Hostname: {hostname}")
        except socket.herror as e:
            print(f"Hostname lookup failed: {e}")
        
        # Get IP WHOIS information
        try:
            obj = IPWhois(ip)
            whois_info = obj.lookup_rdap()
            print(f"Network Name: {whois_info.get('network', {}).get('name', 'Not available')}")
            print(f"ASN: {whois_info.get('asn', 'Not available')}")
            print(f"Country: {whois_info.get('asn_country_code', 'Not available')}")
            print(f"Description: {whois_info.get('asn_description', 'Not available')}")
        except Exception as e:
            print(f"WHOIS lookup failed: {e}")
    
    except ValueError as e:
        print(f"Error: Invalid IP address format. Details: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        ip = input("Enter an IP address to scan: ")
        run(ip)
    except Exception as e:
        print(f"An error occurred while running the script: {e}")
