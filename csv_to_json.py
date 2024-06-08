import csv
import json
# Replace 'file.csv' with the path to your CSV file
csv_file_path = 'DT_Ratings.csv'
# Read the CSV file and convert it into a list of dictionaries
csv_data = []
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)
# Convert the list of dictionaries into a JSON string
json_data = json.dumps(csv_data, indent=2)
# Print the JSON data
print(json_data)
# Replace 'output.json' with the desired path for the output JSON file
output_file_path = 'results.json'
with open(output_file_path, 'w') as jsonfile:
    json.dump(csv_data, jsonfile, indent=2)
