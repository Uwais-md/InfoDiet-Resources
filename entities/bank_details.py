import random
import json
from dotenv import load_dotenv
import os

def generate_ifsc_code(bank_code):
    """
    Generates a random IFSC code for a given bank code.
    IFSC format: BBBB0CCCCCC
    - BBBB: Bank code (e.g., SBIN, IDIB)
    - 0: Reserved character
    - CCCCCC: Branch code (numeric, 6 digits)
    """
    branch_code = f"{random.randint(0, 999999):06d}"
    return f"{bank_code}0{branch_code}"

def generate_account_number(bank_code):
    """
    Generates a random bank account number based on the bank code.
    - For 'SBIN' and 'IDIB': 11-digit account number
    - For other banks: Account number length between 12 and 14 digits
    """
    if bank_code in ['SBIN', 'IDIB']:
        account_number = f"{random.randint(10**10, 10**11 - 1)}"
    else:
        length = random.randint(12, 14)
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return account_number

def generate_bank_details(count):
    """
    Generates a list of dictionaries containing bank account details.
    Each dictionary contains:
    - 'bank_code': Bank code (e.g., SBIN, IDIB)
    - 'account_number': Generated account number
    - 'ifsc_code': Generated IFSC code
    """
    bank_codes = ['SBIN', 'IDIB', 'HDFC', 'ICIC', 'PNB', 'AXIS', 'KARB', 'YESB']
    bank_details_list = []

    for _ in range(count):
        bank_code = random.choice(bank_codes)
        account_number = generate_account_number(bank_code)
        ifsc_code = generate_ifsc_code(bank_code)
        bank_details = {
            'bank_code': bank_code,
            'account_number': account_number,
            'ifsc_code': ifsc_code
        }
        bank_details_list.append(bank_details)

    return bank_details_list

def save_to_json(data, filename):
    """
    Saves data to a JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Loading NUMBER_OF_ENTITIES from environment for uniform number of entities
    load_dotenv()
    NUMBER_OF_ENTITIES = int(os.getenv("NUMBER_OF_ENTITIES"))

    # Generate 1000 bank account details
    bank_details_list = generate_bank_details(NUMBER_OF_ENTITIES)

    # Save the generated bank details to a JSON file
    save_to_json(bank_details_list, "bank_details.json")

    print(f"{NUMBER_OF_ENTITIES} bank account details have been generated and saved to 'bank_details.json'.")
