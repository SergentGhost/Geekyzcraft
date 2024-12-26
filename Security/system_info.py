import subprocess

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"

def system_info():
    """Gathers and displays system information."""
    try:
        print(f"{CYAN}Gathering system information...{RESET}")
        system = subprocess.check_output(["uname", "-a"], text=True).strip()
        print(f"{GREEN}System Information:{RESET} {system}")
    except Exception as e:
        print(f"{RED}Error fetching system information: {e}{RESET}")
