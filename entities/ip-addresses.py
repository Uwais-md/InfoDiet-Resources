import random
import json
from dotenv import load_dotenv
import os

# Function to generate a random IP address
def generate_ip_address():
    # Generate each octet of the IP address (between 0 and 255)
    ip_address = ".".join([str(random.randint(0, 255)) for _ in range(4)])
    return ip_address

# Loading NUMBER_OF_ENTITIES from environment for uniform number of entities
load_dotenv()
NUMBER_OF_ENTITIES = int(os.getenv("NUMBER_OF_ENTITIES"))

# Generate a dictionary of 100 random IP addresses
ip_addresses_dict = [{f"ip_address": generate_ip_address()} for i in range(NUMBER_OF_ENTITIES)]

# Save the dictionary to a JSON file
with open('ip_addresses.json', 'w') as file:
    json.dump(ip_addresses_dict, file, indent=4)

print(f"{NUMBER_OF_ENTITIES} random IP addresses saved to 'ip_addresses.json'")
