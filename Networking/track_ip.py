# Networking.py
import requests
import socket

def track_ip(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        data = response.json()
        print(f"IP Information for {ip_address}:")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country_name', 'N/A')}")
        print(f"Latitude: {data.get('latitude', 'N/A')}")
        print(f"Longitude: {data.get('longitude', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
