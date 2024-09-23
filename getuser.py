import json
import csv

# Input JSON file
JSON_FILE = 'portfolios.json'

# Output CSV file
CSV_FILE = 'originalcsv.csv'

def json_to_csv(json_file, csv_file):
    """Converts JSON data to CSV."""
    
    # Open the JSON file and load data
    with open(json_file, 'r') as json_f:
        data = json.load(json_f)

    # Open CSV file for writing
    with open(csv_file, mode='w', newline='') as csv_f:
        writer = csv.writer(csv_f)

        # Write CSV header
        writer.writerow(['Portfolio ID', 'Password', 'Product ID', 'User ID'])

        # Write data rows
        for entry in data:
            writer.writerow([
                entry['username'],       # Portfolio ID
                entry['password'],       # Password
                entry['workspace_name'], # Product ID
                entry['portfolio_name']  # User ID
            ])

    print(f"Data saved to {csv_file}")

# Execute the conversion
json_to_csv(JSON_FILE, CSV_FILE)
