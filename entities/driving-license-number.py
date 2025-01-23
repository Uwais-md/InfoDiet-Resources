import random
import json
import string
from dotenv import load_dotenv
import os

def generate_driving_licence_numbers(count):
    """
    Generates a list of driving licence numbers in the specified formats.

    Args:
        count (int): Number of licence numbers to generate.

    Returns:
        list: List of driving licence numbers.
    """
    state_codes = ["AN","AP", "AR", "AS","BR", "CG","CH", "DD", "DL", "GA", "GJ", "HP", "HR", "JH", "JK", "KA", "KL", "LA", "LD" "MH", "ML", "MN", "MP", "MZ", "NL", "OD", "PB", "PY", "RJ", "SK", "TG", "TN", "TR", "UK", "UP", "WB"]
    licence_numbers = []

    for _ in range(count):
        state_code = random.choice(state_codes)
        rto_code = f"{random.randint(1, 99):02d}"
        year_of_issue = random.randint(2000, 2023)
        number_sequence = f"{random.randint(1000000, 9999999):07d}"

        # Randomly select a format
        if random.choice([True, False]):
            licence_number = f"{state_code}-{rto_code}{year_of_issue}{number_sequence}"
        else:
            licence_number = f"{state_code}{rto_code} {year_of_issue}{number_sequence}"

        licence_number = {"license_num": licence_number}

        licence_numbers.append(licence_number)

    return licence_numbers

def save_to_json(data, filename):
    """
    Saves data to a JSON file.

    Args:
        data (list): Data to save.
        filename (str): Name of the JSON file.

    Returns:
        None
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Loading NUMBER_OF_ENTITIES from environment for uniform number of entities
    load_dotenv()
    NUMBER_OF_ENTITIES = int(os.getenv("NUMBER_OF_ENTITIES"))

    # Generate 1000 driving licence numbers
    licence_numbers = generate_driving_licence_numbers(NUMBER_OF_ENTITIES)

    # Save the generated licence numbers to a JSON file
    save_to_json(licence_numbers, "driving_licence_numbers.json")

    print(f"{NUMBER_OF_ENTITIES} driving licence numbers have been generated and saved to 'driving_licence_numbers.json'.")
