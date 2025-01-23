import random
import csv
import pandas as pd
import json
from dotenv import load_dotenv
import os

def load_csv_data(filename):
    """
    Loads data from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        list: List of items from the CSV file.
    """
    data = pd.read_csv(filename,).to_numpy()
    # print(data)
    return data

def generate_emails(male_names, female_names, domains, count):
    """
    Generates a list of random emails using names and email domains.

    Args:
        male_names (list): List of male names.
        female_names (list): List of female names.
        domains (list): List of email domains.
        count (int): Number of emails to generate.

    Returns:
        list: List of generated email addresses.
    """
    emails = []
    all_names = male_names[0] + female_names[0]
    for _ in range(count):
        name = random.choice(all_names).lower().replace(" ", "")
        number = random.randint(1, 888)
        domain = random.choice(domains)
        email = f"{name}{number}@{domain[1]}"
        emails.append({"email":email})
    return emails

def save_to_json(data, filename):
    """
    Saves data to a CSV file.

    Args:
        data (list): Data to save.
        filename (str): Name of the CSV file.

    Returns:
        None
    """
    # Save the list to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Loading NUMBER_OF_ENTITIES from environment for uniform number of entities
    load_dotenv()
    NUMBER_OF_ENTITIES = int(os.getenv("NUMBER_OF_ENTITIES"))
    # print(int(NUMBER_OF_ENTITIES))

    # Load names and domains from CSV files
    female_names = load_csv_data("./Indian Female Names/Indian-Female-Names.csv")
    male_names = load_csv_data("./Indian Male Names/Indian-Male-Names.csv")
    domains = load_csv_data("email-domain.csv")

    # Generate 1000 emails
    emails = generate_emails(male_names, female_names, domains, NUMBER_OF_ENTITIES)

    # Save the generated emails to a CSV file
    save_to_json(emails, "emails.json")

    print(f"{NUMBER_OF_ENTITIES} emails have been generated and saved to 'emails.json'.")
