import json
import random

def load_bank_details(filename):
    """
    Loads bank details from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def luhn_checksum(card_number):
    """
    Calculates the Luhn checksum for a card number.
    """
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_check_digit(card_number):
    """
    Generates the check digit for a card number using the Luhn algorithm.
    """
    check_digit = luhn_checksum(int(card_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit

def generate_card_number(bin_code, account_number):
    """
    Generates a 16-digit card number using the BIN, account number, and a check digit.
    """
    # Ensure the account number is 10 digits
    account_number = account_number[-10:].zfill(10)
    partial_card_number = f"{bin_code}{account_number}"
    check_digit = generate_check_digit(partial_card_number)
    return f"{partial_card_number}{check_digit}"

def generate_cvv():
    """
    Generates a random 3-digit CVV code.
    """
    return f"{random.randint(100, 999)}"

def generate_card_details(bank_details):
    """
    Generates card details for each user in the bank details.
    """
    card_details_list = []
    # Example BIN codes for Indian banks
    bin_codes = {
        'SBIN': '400016',  # State Bank of India
        'HDFC': '403276',  # HDFC Bank
        'ICIC': '402653',  # ICICI Bank
        'PNB': '552100',   # Punjab National Bank
        'AXIS': '508126',  # Axis Bank
        'KARB': '539150',  # Karnataka Bank
        'YESB': '507865',  # Yes Bank
        'IDIB': '432808'   # Indian Bank
    }
    for user in bank_details:
        bank_code = user['bank_code']
        bank_ifsc = user['ifsc_code']
        account_number = user['account_number']
        bin_code = bin_codes.get(bank_code, '400000')  # Default BIN if bank code not found
        card_number = generate_card_number(bin_code, account_number)
        cvv = generate_cvv()
        card_details = {
            'bank_code': bank_code,
            'ifsc_code': bank_ifsc,
            'account_number': account_number,
            'card_number': card_number,
            'cvv': cvv
        }
        card_details_list.append(card_details)
    return card_details_list

def save_to_json(data, filename):
    """
    Saves data to a JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Load bank details from the JSON file
    bank_details = load_bank_details('bank_details.json')

    # Generate card details
    card_details_list = generate_card_details(bank_details)

    # Save the generated card details to a JSON file
    save_to_json(card_details_list, 'bank_details.json')

    print("Card details have been generated and saved to 'bank_details.json'.")
