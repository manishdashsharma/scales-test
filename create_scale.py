import requests
import json
import os

url = "http://127.0.0.1:8001//v1/voc/scale-management/?type=save_scale_details"

# Replace these with actual portfolio usernames if available
credits = [
    {
        "portfolio": "VOCAB10170",
        "portfolio_username": "d9ov9Z11yNCW"
    },
    {
        "portfolio": "VOCAB10171",
        "portfolio_username": "ez2hkKbrWHbA"
    },
    {
        "portfolio": "VOCAB10172",
        "portfolio_username": "kYzzffiQcDow"
    },
    {
        "portfolio": "VOCAB10173",
        "portfolio_username": "V0HjqhyZFm4D"
    },
    {
        "portfolio": "VOCAB10174",
        "portfolio_username": "hsup8Vsy752X"
    },
    {
        "portfolio": "VOCAB10175",
        "portfolio_username": "y5yH6zRRl34B"
    },
    {
        "portfolio": "VOCAB10176",
        "portfolio_username": "QpBcxMa0MDHi"
    },
    {
        "portfolio": "VOCAB10177",
        "portfolio_username": "iCVVKWAk86dG"
    },
    {
        "portfolio": "VOCAB10178",
        "portfolio_username": "S3oRHk7Dzc7R"
    },
    {
        "portfolio": "VOCAB10179",
        "portfolio_username": "0nBjRW7LOMRB"
    },
    {
        "portfolio": "VOCAB10180",
        "portfolio_username": "0fDtTNu2jGlA"
    },
    {
        "portfolio": "VOCAB10181",
        "portfolio_username": "rBzk7U4WiqxZ"
    },
    {
        "portfolio": "VOCAB10182",
        "portfolio_username": "QmqYINTXEypI"
    },
    {
        "portfolio": "VOCAB10183",
        "portfolio_username": "ryr4zQZzPYuN"
    },
    {
        "portfolio": "VOCAB10184",
        "portfolio_username": "62jLOavzasoW"
    },
    {
        "portfolio": "VOCAB10185",
        "portfolio_username": "rYfTEjftvUVB"
    },
    {
        "portfolio": "VOCAB10186",
        "portfolio_username": "YvuLDvjMnh97"
    },
    {
        "portfolio": "VOCAB10187",
        "portfolio_username": "XXMl0uZCGSMj"
    },
    {
        "portfolio": "VOCAB10188",
        "portfolio_username": "o411o8jD9enE"
    },
    {
        "portfolio": "VOCAB10189",
        "portfolio_username": "MyEBWqRoYaaB"
    },
    {
        "portfolio": "VOCAB10190",
        "portfolio_username": "Z5IHEuZ0Ipja"
    },
    {
        "portfolio": "VOCAB10191",
        "portfolio_username": "hNvqyQ1E7RSp"
    },
    {
        "portfolio": "VOCAB10192",
        "portfolio_username": "1k9csACDnQVx"
    },
    {
        "portfolio": "VOCAB10193",
        "portfolio_username": "FXvf9ALmNLsU"
    },
    {
        "portfolio": "VOCAB10194",
        "portfolio_username": "bp2b6D53k5ME"
    },
    {
        "portfolio": "VOCAB10195",
        "portfolio_username": "6W1Z4DcMcLaK"
    },
    {
        "portfolio": "VOCAB10196",
        "portfolio_username": "dUYMsx6nIGgK"
    },
    {
        "portfolio": "VOCAB10197",
        "portfolio_username": "GhrgmQFKx38K"
    },
    {
        "portfolio": "VOCAB10198",
        "portfolio_username": "UI0dfg5fSlUP"
    },
    {
        "portfolio": "VOCAB10199",
        "portfolio_username": "4insVpoapg9g"
    },
    {
        "portfolio": "VOCAB10200",
        "portfolio_username": "NLx8pldSsyVb"
    },
    {
        "portfolio": "VOCAB10201",
        "portfolio_username": "yQqf87T4aXMF"
    },
    {
        "portfolio": "VOCAB10202",
        "portfolio_username": "BPFx3XDBi2Tx"
    },
    {
        "portfolio": "VOCAB10203",
        "portfolio_username": "uzus452dkxlx"
    },
    {
        "portfolio": "VOCAB10204",
        "portfolio_username": "dj8mRmmz0j4T"
    },
    {
        "portfolio": "VOCAB10205",
        "portfolio_username": "ghRybTEBqgeY"
    },
    {
        "portfolio": "VOCAB10206",
        "portfolio_username": "cRJVHoHh0VAn"
    },
    {
        "portfolio": "VOCAB10207",
        "portfolio_username": "vDWnvGuJgUCa"
    },
    {
        "portfolio": "VOCAB10208",
        "portfolio_username": "56MwrmxTsdHd"
    },
    {
        "portfolio": "VOCAB10209",
        "portfolio_username": "hBbp6atDankW"
    },
    {
        "portfolio": "VOCAB10210",
        "portfolio_username": "o1erMDICo0fL"
    },
    {
        "portfolio": "VOCAB10211",
        "portfolio_username": "9JgzX6bFARdR"
    },
    {
        "portfolio": "VOCAB10212",
        "portfolio_username": "fDpgJlxJ1qWD"
    },
    {
        "portfolio": "VOCAB10213",
        "portfolio_username": "x9vrJCe7JMTo"
    },
    {
        "portfolio": "VOCAB10214",
        "portfolio_username": "4KBTLxsgVXcQ"
    },
    {
        "portfolio": "VOCAB10215",
        "portfolio_username": "H1Kv5aMnvlKi"
    },
    {
        "portfolio": "VOCAB10216",
        "portfolio_username": "vgONPzlpzAgq"
    },
    {
        "portfolio": "VOCAB10217",
        "portfolio_username": "tGJNc1o9CF0n"
    },
    {
        "portfolio": "VOCAB10218",
        "portfolio_username": "j7gzEN0nU1vN"
    },
    {
        "portfolio": "VOCAB10219",
        "portfolio_username": "BQDpdsKSBEYR"
    }
]

# Payload template
payload_template = {
    "workspace_id": "66b9ab8f8e615ce827af9115",
    "username": "VOCAB",
    "portfolio": "",
    "portfolio_username": "",
}

# Directories for saving responses
success_dir = "success_responses"
error_dir = "error_responses"

# Create directories if they don't exist
os.makedirs(success_dir, exist_ok=True)
os.makedirs(error_dir, exist_ok=True)

def save_scale_details(credits):
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

            # print(f"Response: {json.dumps(res, indent=4)}")

            # Check the success status in the response
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

# Call the function to save scale details
save_scale_details(credits)