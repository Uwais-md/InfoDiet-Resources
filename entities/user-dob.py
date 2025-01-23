import random
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

def generate_random_dob(count):
    """
    Generates a list of random dates of birth in specified formats (DD-MM-YYYY and DD/MM/YYYY).

    Args:
        count (int): Number of dates of birth to generate.

    Returns:
        list: List of dates of birth in mixed formats.
    """
    dob_list = []
    for _ in range(count):
        # Generate a random date of birth
        start_date = datetime(1960, 1, 1)
        end_date = datetime(2024, 1, 1)
        random_days = random.randint(0, (end_date - start_date).days)
        random_dob = start_date + timedelta(days=random_days)

        # Randomly choose a format
        if random.choice([True, False]):
            dob = {"dob": random_dob.strftime("%d-%m-%Y")}
        else:
            dob = {"dob": random_dob.strftime("%d/%m/%Y")}

        dob_list.append(dob)

    return dob_list

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

    # Generate 1000 random dates of birth
    dob_list = generate_random_dob(NUMBER_OF_ENTITIES)

    # Save the generated dates of birth to a JSON file
    save_to_json(dob_list, "user_dob.json")

    print(f"{NUMBER_OF_ENTITIES} random dates of birth have been generated and saved to 'user_dob.json'.")
