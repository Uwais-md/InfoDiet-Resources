import random
import json

def generate_random_numbers(count, digit_length):
    """
    Generates a list of random numbers with a specified digit length.

    Args:
        count (int): Number of random numbers to generate.
        digit_length (int): Number of digits in each random number.

    Returns:
        list: List of random numbers as strings.
    """
    random_numbers = [
        {"aadhar": str(random.randint(10**(digit_length - 1), (10**digit_length) - 1))}
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
    # Generate 3000 random 12-digit numbers
    random_numbers = generate_random_numbers(1000, 12)

    # Save the generated numbers to a JSON file
    save_to_json(random_numbers, "aadhar_number.json")

    print("1000 random 12-digit numbers have been generated and saved to 'random_numbers.json'.")
