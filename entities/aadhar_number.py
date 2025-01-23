import random
import json
from dotenv import load_dotenv
import os

def format_aadhar_number(number):
    """
    Formats a 12-digit number into one of three random formats:
    - Continuous (e.g., 437623083136)
    - Space-separated (e.g., 4376 2308 3136)
    - Hyphen-separated (e.g., 4376-2308-3136)

    Args:
        number (str): A 12-digit number as a string.

    Returns:
        str: Formatted Aadhaar number.
    """
    formats = [
        "{}",  # Continuous
        "{} {} {}",  # Space-separated
        "{}-{}-{}"   # Hyphen-separated
    ]
    selected_format = random.choice(formats)
    return selected_format.format(number[:4], number[4:8], number[8:])

def generate_random_numbers(count, digit_length):
    """
    Generates a list of random numbers with a specified digit length
    and formats them randomly.

    Args:
        count (int): Number of random numbers to generate.
        digit_length (int): Number of digits in each random number.

    Returns:
        list: List of formatted random numbers as strings.
    """
    random_numbers = [
        {"aadhar": format_aadhar_number(str(random.randint(10**(digit_length - 1), (10**digit_length) - 1)))}
        for _ in range(count)
    ]
    return random_numbers

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
    
    # Generate 1000 random 12-digit Aadhaar numbers with random formats
    random_numbers = generate_random_numbers(NUMBER_OF_ENTITIES, 12)

    # Save the generated numbers to a JSON file
    save_to_json(random_numbers, "aadhar_number.json")

    print(f"{NUMBER_OF_ENTITIES} random Aadhaar numbers with varying formats have been generated and saved to 'aadhar_number.json'.")
