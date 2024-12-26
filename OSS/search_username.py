import requests

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def search_username(username):
    """Searches for a username or similar usernames on the internet."""
    print(f"{CYAN}Searching for username: {username}{RESET}")
    try:
        platforms = {
            "GitHub": f"https://github.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}/"
        }

        for platform, url in platforms.items():
            response = requests.head(url, allow_redirects=True)
            if response.status_code == 200:
                print(f"{GREEN}Found on {platform}: {url}{RESET}")
            else:
                print(f"{YELLOW}Not found on {platform}.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
