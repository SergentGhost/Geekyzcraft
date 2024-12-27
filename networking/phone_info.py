import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(phone_number):
    """Extracts information about the given phone number."""
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid phone number."}
        
        # Gather information
        info = {
            "Number": phone_number,
            "Country": geocoder.description_for_number(parsed_number, "en"),
            "Carrier": carrier.name_for_number(parsed_number, "en"),
            "Time Zones": timezone.time_zones_for_number(parsed_number),
            "Valid": "Yes" if phonenumbers.is_valid_number(parsed_number) else "No"
        }
        return info
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

def display_phone_info(info):
    """Displays the phone information in a readable format."""
    if "error" in info:
        print(f"Error: {info['error']}")
    else:
        print("Phone Number Information:")
        print("=========================")
        for key, value in info.items():
            print(f"{key}: {value}")

def run():
    """Main function for the Phone Information Tool."""
    print("Phone Number Information Tool")
    print("=============================")
    phone_number = input("Enter the phone number (with country code, e.g., +1234567890): ")

    info = get_phone_info(phone_number)
    display_phone_info(info)
