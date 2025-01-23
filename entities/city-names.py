import json

def convert_json_object_to_list(input_json_file, output_json_file):
    # Load the input JSON object
    with open(input_json_file, mode='r') as file:
        data = json.load(file)
    
    # Convert the object into a list of objects
    result = list(data.values())
    
    # Save the list of objects to the output file
    with open(output_json_file, mode='w') as file:
        json.dump(result, file, indent=4)

# Example usage
input_json_file = 'city-names.json'  # Replace with the path to your input JSON file
output_json_file = 'city-names.json'  # Replace with the path for the output JSON file
convert_json_object_to_list(input_json_file, output_json_file)
