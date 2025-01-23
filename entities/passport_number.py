import random
import json
from dotenv import load_dotenv
import os

def generate_custom_strings(count):
    """
    Generates a list of strings based on the given constraints:
    - 8 characters long.
    - First character: Uppercase alphabet.
    - Next two characters: A number (first digit 1-9, second digit 0-9).
    - Zero or one whitespace character.
    - Next four characters: Any digit (0-9).
    - Last character: Any digit (1-9).

    Args:
        count (int): Number of strings to generate.

    Returns:
        list: List of generated strings.
    """
    strings = []
    for _ in range(count):
        first_char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        number_part = f"{random.randint(1, 9)}{random.randint(0, 9)}"
        whitespace = " " if random.choice([True, False]) else ""
        middle_part = "".join([str(random.randint(0, 9)) for _ in range(4)])
        last_char = str(random.randint(1, 9))
        custom_string = f"{first_char}{number_part}{whitespace}{middle_part}{last_char}"
        custom_string = {"passport_num" : custom_string}
        strings.append(custom_string)
    return strings

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

    # Generate 1000 custom strings
    passport_number = generate_custom_strings(NUMBER_OF_ENTITIES)

    # Save the generated strings to a JSON file
    save_to_json(passport_number, "passport_number.json")

    print(f"{NUMBER_OF_ENTITIES} custom strings have been generated and saved to 'passport_number.json'.")
