from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """Scans the given IP range for connected devices."""
    print(f"Scanning network in the range {ip_range}...\n")

    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and receive responses
    answered, _ = srp(arp_request_broadcast, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def display_devices(devices):
    """Displays the connected devices in a tabular format."""
    if devices:
        print("Connected Devices:")
        print(f"{'IP Address':<20}{'MAC Address':<20}")
        print("-" * 40)
        for device in devices:
            print(f"{device['ip']:<20}{device['mac']:<20}")
    else:
        print("No devices found.")

def run():
    """Main function for the Network Scanner."""
    print("Wi-Fi Network Scanner")
    print("=====================")
    ip_range = input("Enter the IP range (e.g., 192.168.1.0/24): ")

    try:
        devices = scan_network(ip_range)
        display_devices(devices)
    except Exception as e:
        print(f"An error occurred: {e}")
