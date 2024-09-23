import csv
import json
import requests

# API URL
API_URL = "https://100093.pythonanywhere.com/api/portfoliologin"

# Input CSV file
CSV_FILE = "originalcsv.csv"

# Output JSON file
OUTPUT_FILE = "portfolios.json"

def read_csv(file_path):
    """Reads the CSV file and returns a list of portfolio credentials."""
    portfolios = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            portfolios.append({
                "username": row["Portfolio ID"],   # Mapping "Portfolio ID" to "username"
                "password": row["Password"],       # Mapping "Password" to "password"
                "workspace_name": row["Product ID"]  # Mapping "Product ID" to "workspace_name"
            })
    return portfolios

def send_post_request(portfolio_data):
    """Sends a POST request to the API and returns the response."""
    payload = {
        "workspace_name": portfolio_data["workspace_name"],
        "portfolio": portfolio_data["username"],  # Send "username" as portfolio to API
        "password": portfolio_data["password"],
        "username": "false"  # Assuming 'username' in API payload is always "false"
    }
    response = requests.post(API_URL, json=payload)
    
    # If the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for portfolio {portfolio_data['username']}. Status Code: {response.status_code}")
        return None

def save_to_json(data, file_path):
    """Saves the given data to a JSON file."""
    with open(file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    # Read the CSV file
    portfolios = read_csv(CSV_FILE)
    
    # List to store the processed portfolio info
    json_data = []
    
    # Loop over each portfolio and send a POST request
    for portfolio in portfolios:
        response_data = send_post_request(portfolio)
        
        if response_data:
            # Extract the username array and use the first element as portfolio_name
            portfolio_name = response_data.get("portfolio_info", {}).get("username", [""])[0]
            
            # Add the required fields to the list
            json_data.append({
                "username": portfolio["username"],
                "password": portfolio["password"],
                "workspace_name": portfolio["workspace_name"],
                "portfolio_name": portfolio_name  # Set portfolio_name to the first element of the "username" array
            })
    
    # Save the collected data to the JSON file
    save_to_json(json_data, OUTPUT_FILE)
    print(f"Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
