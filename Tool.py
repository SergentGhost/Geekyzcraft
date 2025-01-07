## USE THIS WITH CAUTION !!

# main_tool.py
import os
import sys
import importlib

# Colors for Linux terminal
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"

def display_banner():
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
    
def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def display_menu():
    print("""
Multi-Purpose Tool
-------------------
1. Networking Tools
2. OS Tools
3. Security Tools
4. Exit
    """)

def import_and_run(module_name, function_name):
    try:
        # Dynamically import the module
        module = importlib.import_module(module_name)
        # Retrieve the function from the module
        func = getattr(module, function_name)
        func()
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found. Check your directory structure.")
    except AttributeError:
        print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def networking_tools():
    tools = {
        '1': ('ip_check', 'run'),
        '2': ('port_scan', 'run'),
        '3': ('vulnerability_scanner', 'run'),
        '4': ('network_scanner', 'run'),
        '5': ('phone_info', 'run')
    }
    print("Networking Tools:")
    for key, value in tools.items():
        print(f"{key}. {value[0]}")
    choice = input("Select a tool: ")
    if choice in tools:
        module, func = tools[choice]
        import_and_run(f"networking.{module}", func)
    else:
        print("Invalid choice.")

def os_tools():
    tools = {
        '1': ('username', 'run'),
        '2': ('website_history', 'run'),
        '3': ('tool3', 'run'),
        '4': ('tool4', 'run'),
        '5': ('tool5', 'run')
    }
    print("OS Tools:")
    for key, value in tools.items():
        print(f"{key}. {value[0]}")
    choice = input("Select a tool: ")
    if choice in tools:
        module, func = tools[choice]
        import_and_run(f"os.{module}", func)
    else:
        print("Invalid choice.")

def security_tools():
    tools = {
        '1': ('tool1', 'run'),
        '2': ('tool2', 'run'),
        '3': ('tool3', 'run'),
        '4': ('tool4', 'run'),
        '5': ('tool5', 'run')
    }
    print("Security Tools:")
    for key, value in tools.items():
        print(f"{key}. {value[0]}")
    choice = input("Select a tool: ")
    if choice in tools:
        module, func = tools[choice]
        import_and_run(f"security.{module}", func)
    else:
        print("Invalid choice.")

def main():
    while True:
        clear_screen()
        display_banner()
        display_menu()
        choice = input("Select an option: ")
        clear_screen()
        display_banner()
        if choice == '1':
            networking_tools()
        elif choice == '2':
            os_tools()
        elif choice == '3':
            security_tools()
        elif choice == '4':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

