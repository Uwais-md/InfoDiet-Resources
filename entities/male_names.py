import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file and convert to JSON
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]  # Convert each row into a dictionary
    
    # Save the JSON data to a file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = 'Indian Male Names/Indian-Male-Names.csv'  # Replace with your CSV file path
json_file_path = 'male_names.json'  # Replace with your desired JSON output file path
csv_to_json(csv_file_path, json_file_path)
