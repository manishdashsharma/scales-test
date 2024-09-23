import requests
import json
import os

# ---- Helper functions ----

def load_existing_data(filename):
    """Load data from JSON file if exists."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_data_to_json(filename, data):
    """Save data to JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# ---- Part 1: Create Users ----

def create_users(credentials_list, success_json_filename, failed_json_filename):
    url = "http://127.0.0.1:8001/v1/voc/user-management/?type=authenticate_user"
    
    # Load existing data from the JSON files
    success_data = load_existing_data(success_json_filename)
    failed_data = load_existing_data(failed_json_filename)

    for credentials in credentials_list:
        print(f"Creating user {credentials['username']}...")
        payload = {
            "workspace_name": "VOCABC",
            "portfolio": credentials["username"],
            "password": credentials["password"],
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            print(f"Request failed for user {credentials['username']}: {e}")
            failed_data.append({"portfolio": credentials["username"], "error": str(e)})
            continue

        try:
            res = response.json()
            portfolio_username = res["response"]["portfolio_username"]
            print(f"Created user {portfolio_username}")
        except (ValueError, KeyError) as e:
            print(f"Failed to parse response for user {credentials['username']}: {response.text}")
            failed_data.append({"portfolio": credentials["username"], "error": f"Failed to parse response: {response.text}"})
            continue

        if res.get("success"):
            print(f"User {credentials['username']} created successfully")
            # Add the new data to the success data list
            success_data.append({"portfolio": credentials["username"], "portfolio_username": portfolio_username})
        else:
            error_message = res.get('message', 'Unknown error')
            print(f"Failed to create user {credentials['username']}: {error_message}")
            failed_data.append({"portfolio": credentials["username"], "error": error_message})

    # Save updated data to the JSON files
    save_data_to_json(success_json_filename, success_data)
    save_data_to_json(failed_json_filename, failed_data)

    return success_data  # Return the success data for use in part 2

# ---- Part 2: Save Scale Details ----

def save_scale_details(credits, success_dir="success_responses", error_dir="error_responses"):
    """Save scale details using the success data."""
    url = "http://127.0.0.1:8001/v1/voc/scale-management/?type=save_scale_details_type"
    
    # Create directories if they don't exist
    os.makedirs(success_dir, exist_ok=True)
    os.makedirs(error_dir, exist_ok=True)

    payload_template = {
        "workspace_id": "66c3a354c0c8c6fbadd5fed4",
        "username": "VOCABC",
        "portfolio": "",
        "portfolio_username": "",
        "type_of_scale": "likert"
    }

    for credit in credits:
        # Use .copy() to ensure the original template isn't modified
        payload = payload_template.copy()
        payload["portfolio"] = credit["portfolio"]
        payload["portfolio_username"] = credit["portfolio_username"]
        
        print(f"Processing portfolio: {credit['portfolio']} with username: {credit['portfolio_username']}")
        print(f"Payload: {json.dumps(payload, indent=4)}")

        try:
            # Make the POST request
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

            # Parse the JSON response
            res = response.json()

            if res.get("success"):
                print(f"Scale details saved successfully for portfolio: {credit['portfolio']}")
                # Save successful response to a JSON file
                success_filename = os.path.join(success_dir, f"{credit['portfolio']}.json")
                with open(success_filename, 'w') as f:
                    json.dump(res, f, indent=4)
            else:
                print(f"Failed to save scale details for portfolio: {credit['portfolio']}, Reason: {res.get('message', 'Unknown error')}")
                # Save failed response to a JSON file
                error_filename = os.path.join(error_dir, f"{credit['portfolio']}_error.json")
                with open(error_filename, 'w') as f:
                    json.dump(res, f, indent=4)

        except requests.exceptions.RequestException as e:
            # Handle request errors (e.g., network issues)
            print(f"Request failed for portfolio: {credit['portfolio']}, Error: {str(e)}")
            # Save request error details to a JSON file
            error_filename = os.path.join(error_dir, f"{credit['portfolio']}_request_error.json")
            with open(error_filename, 'w') as f:
                json.dump({"error": str(e)}, f, indent=4)

# ---- Combined Execution ----

# Define the credentials and file names
credentials_list = [
    {"username": "VOCABC10052", "password": "VocaB17309*"},
    {"username": "VOCABC10053", "password": "VocaB22638*"}
]
success_json_filename = "created_users.json"
failed_json_filename = "failed_users.json"

# Step 1: Create Users and get the success data
success_data = create_users(credentials_list, success_json_filename, failed_json_filename)

# Step 2: Use the success data to save scale details
if success_data:
    save_scale_details(success_data)
else:
    print("No successful user creation data to proceed with scale details.")
