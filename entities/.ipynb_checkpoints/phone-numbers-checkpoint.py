import random
import json

def generate_mobile_number():
    # Mobile number starts with 7, 8, or 9, followed by 9 random digits.
    mobile_number = str(random.choice([7, 8, 9])) + ''.join([str(random.randint(0, 9)) for _ in range(9)])

    # Formats to return
    formats = [
        f"+91 {mobile_number}",
        f"+91{mobile_number}",
        f"+91 {mobile_number[:5]} {mobile_number[5:]}",
        f"+91{mobile_number[:5]} {mobile_number[5:]}",
        f"91 {mobile_number}",
        f"91{mobile_number}",
        f"91 {mobile_number[:5]} {mobile_number[5:]}",
        f"91{mobile_number[:5]} {mobile_number[5:]}",
        f"0{mobile_number}",
        f"{mobile_number}",
        f"{mobile_number[:5]} {mobile_number[5:]}",
        f"{mobile_number[:3]} {mobile_number[3:6]} {mobile_number[6:]}"
    ]
    
    return random.choice(formats)

# Generate a list of 100 random mobile numbers
random_mobile_numbers = [{"phone": generate_mobile_number()} for _ in range(1000)]

# Save the list to a JSON file
with open('phone_numbers.json', 'w') as file:
    json.dump(random_mobile_numbers, file, indent=4)

print("Random mobile numbers saved to 'phone_numbers.json'")
