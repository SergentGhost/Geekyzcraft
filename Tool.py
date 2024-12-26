import os
import logging
from datetime import datetime
import requests
import socket

# Setup for colors and logging
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"

logging.basicConfig(filename="errors.log", level=logging.ERROR)

def log_error(message):
    logging.error(f"{datetime.now()} - {message}")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Displays a fancy banner."""
    print(f"{YELLOW}{BOLD}")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░     ░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░")
    print("▒▒  ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒   ▒   ▒▒▒   ▒▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒    ")
    print("▓   ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓▓  ▓▓▓   ▓▓   ▓   ▓▓▓   ▓   ▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓▓")
    print("▓   ▓▓▓      ▓         ▓▓         ▓▓     ▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓   ▓▓▓▓")
    print("▓▓   ▓▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓▓")
    print("███      ███████     ██████     ████   ██   ████   ████  ██   █    ██   ████    ")
    print("███████████████████████████████████████████████   ██████████████████████████████")
    print(f"{RESET}")
    
def load_oss_tools():
    # Placeholder for OSS tools
    print(f"{CYAN}OSS tools are under construction...{RESET}")
    input(f"{YELLOW}Press Enter to return to the main menu...{RESET}")

def load_security_tools():
    # Placeholder for Security tools
    print(f"{CYAN}Security tools are under construction...{RESET}")
    input(f"{YELLOW}Press Enter to return to the main menu...{RESET}")

    # tool.py

def load_networking_tools():
    from Networking import track_ip  # Import the function directly
    return track_ip


# Main menu to choose categories
def menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{CYAN}{BOLD}Choose a Category:{RESET}")
        print("1. Networking")
        print("2. OSS")
        print("3. Security")
        print("4. Exit")

        choice = input(f"\n{YELLOW}Enter your choice: {RESET}")
        
        if choice == "1":
            track_ip = load_networking_tools()  # Load the track_ip function here
            networking_menu(track_ip)
        elif choice == "2":
            load_oss_tools()
        elif choice == "3":
            load_security_tools()
        elif choice == "4":
            print(f"{GREEN}Exiting the tool. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            input(f"\n{YELLOW}Press Enter to return to the menu...{RESET}")

# Networking specific menu
def networking_menu(track_ip):
    while True:
        clear_screen()
        print_banner()
        print(f"{CYAN}{BOLD}Networking Tools:{RESET}")
        print("1. Track IP")
        print("2. Back to Main Menu")

        choice = input(f"\n{YELLOW}Enter your choice: {RESET}")
        
        if choice == "1":
            ip = input(f"{CYAN}Enter the IP address: {RESET}")
            track_ip(ip)
        elif choice == "2":
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            input(f"\n{YELLOW}Press Enter to return to the networking menu...{RESET}")

if __name__ == "__main__":
    menu()
