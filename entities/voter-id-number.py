import random
import string
import json
from dotenv import load_dotenv
import os

def generate_random_strings(count):
    """
    Generates a list of random strings.
    Each string contains:
        - First 5 characters: Random capital alphabets.
        - Next 4 characters: Random 4-digit number.
        - Last character: Single random capital alphabet.

    Args:
        count (int): Number of random strings to generate.

    Returns:
        list: List of random strings.
    """
    random_strings = []
    for _ in range(count):
        first_part = ''.join(random.choices(string.ascii_uppercase, k=3))
        middle_part = str(random.randint(1010000, 9909099))
        random_string = first_part + middle_part
        data = {"voter_id" : random_string}
        random_strings.append(data)
    return random_strings

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

    # Generate 3000 random strings
    random_strings = generate_random_strings(NUMBER_OF_ENTITIES)

    # Save the generated strings to a JSON file
    save_to_json(random_strings, "voter_id.json")

    print(f"{NUMBER_OF_ENTITIES} random strings have been generated and saved to 'voter_id.json'.")
