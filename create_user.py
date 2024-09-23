import requests
import json
import os



credentials_list = [
    {
        "username": "VOCAB10170",
        "password": "VocaZ1985@",
        "workspace_name": "VOCAB",
        "portfolio_name": "d9ov9Z11yNCW"
    },
    {
        "username": "VOCAB10171",
        "password": "VocaZ1994@",
        "workspace_name": "VOCAB",
        "portfolio_name": "ez2hkKbrWHbA"
    },
    {
        "username": "VOCAB10172",
        "password": "VocaZ2000@",
        "workspace_name": "VOCAB",
        "portfolio_name": "kYzzffiQcDow"
    },
    {
        "username": "VOCAB10173",
        "password": "VocaZ2002@",
        "workspace_name": "VOCAB",
        "portfolio_name": "V0HjqhyZFm4D"
    },
    {
        "username": "VOCAB10174",
        "password": "VocaZ2010@",
        "workspace_name": "VOCAB",
        "portfolio_name": "hsup8Vsy752X"
    },
    {
        "username": "VOCAB10175",
        "password": "VocaZ2013@",
        "workspace_name": "VOCAB",
        "portfolio_name": "y5yH6zRRl34B"
    },
    {
        "username": "VOCAB10176",
        "password": "VocaZ2020@",
        "workspace_name": "VOCAB",
        "portfolio_name": "QpBcxMa0MDHi"
    },
    {
        "username": "VOCAB10177",
        "password": "VocaZ2025@",
        "workspace_name": "VOCAB",
        "portfolio_name": "iCVVKWAk86dG"
    },
    {
        "username": "VOCAB10178",
        "password": "VocaZ2029@",
        "workspace_name": "VOCAB",
        "portfolio_name": "S3oRHk7Dzc7R"
    },
    {
        "username": "VOCAB10179",
        "password": "VocaZ2038@",
        "workspace_name": "VOCAB",
        "portfolio_name": "0nBjRW7LOMRB"
    },
    {
        "username": "VOCAB10180",
        "password": "VocaZ2044@",
        "workspace_name": "VOCAB",
        "portfolio_name": "0fDtTNu2jGlA"
    },
    {
        "username": "VOCAB10181",
        "password": "VocaZ2046@",
        "workspace_name": "VOCAB",
        "portfolio_name": "rBzk7U4WiqxZ"
    },
    {
        "username": "VOCAB10182",
        "password": "VocaZ2054@",
        "workspace_name": "VOCAB",
        "portfolio_name": "QmqYINTXEypI"
    },
    {
        "username": "VOCAB10183",
        "password": "VocaZ2057@",
        "workspace_name": "VOCAB",
        "portfolio_name": "ryr4zQZzPYuN"
    },
    {
        "username": "VOCAB10184",
        "password": "VocaZ2064@",
        "workspace_name": "VOCAB",
        "portfolio_name": "62jLOavzasoW"
    },
    {
        "username": "VOCAB10185",
        "password": "VocaZ2069@",
        "workspace_name": "VOCAB",
        "portfolio_name": "rYfTEjftvUVB"
    },
    {
        "username": "VOCAB10186",
        "password": "VocaZ2073@",
        "workspace_name": "VOCAB",
        "portfolio_name": "YvuLDvjMnh97"
    },
    {
        "username": "VOCAB10187",
        "password": "VocaZ2082@",
        "workspace_name": "VOCAB",
        "portfolio_name": "XXMl0uZCGSMj"
    },
    {
        "username": "VOCAB10188",
        "password": "VocaZ2088@",
        "workspace_name": "VOCAB",
        "portfolio_name": "o411o8jD9enE"
    },
    {
        "username": "VOCAB10189",
        "password": "VocaZ2090@",
        "workspace_name": "VOCAB",
        "portfolio_name": "MyEBWqRoYaaB"
    },
    {
        "username": "VOCAB10190",
        "password": "VocaZ2096@",
        "workspace_name": "VOCAB",
        "portfolio_name": "Z5IHEuZ0Ipja"
    },
    {
        "username": "VOCAB10191",
        "password": "VocaZ2093@",
        "workspace_name": "VOCAB",
        "portfolio_name": "hNvqyQ1E7RSp"
    },
    {
        "username": "VOCAB10192",
        "password": "VocaZ2098@",
        "workspace_name": "VOCAB",
        "portfolio_name": "1k9csACDnQVx"
    },
    {
        "username": "VOCAB10193",
        "password": "VocaZ2099@",
        "workspace_name": "VOCAB",
        "portfolio_name": "FXvf9ALmNLsU"
    },
    {
        "username": "VOCAB10194",
        "password": "VocaZ2105@",
        "workspace_name": "VOCAB",
        "portfolio_name": "bp2b6D53k5ME"
    },
    {
        "username": "VOCAB10195",
        "password": "VocaZ2113@",
        "workspace_name": "VOCAB",
        "portfolio_name": "6W1Z4DcMcLaK"
    },
    {
        "username": "VOCAB10196",
        "password": "VocaZ2115@",
        "workspace_name": "VOCAB",
        "portfolio_name": "dUYMsx6nIGgK"
    },
    {
        "username": "VOCAB10197",
        "password": "VocaZ2122@",
        "workspace_name": "VOCAB",
        "portfolio_name": "GhrgmQFKx38K"
    },
    {
        "username": "VOCAB10198",
        "password": "VocaZ2126@",
        "workspace_name": "VOCAB",
        "portfolio_name": "UI0dfg5fSlUP"
    },
    {
        "username": "VOCAB10199",
        "password": "VocaZ2135@",
        "workspace_name": "VOCAB",
        "portfolio_name": "4insVpoapg9g"
    },
    {
        "username": "VOCAB10200",
        "password": "VocaZ2138@",
        "workspace_name": "VOCAB",
        "portfolio_name": "NLx8pldSsyVb"
    },
    {
        "username": "VOCAB10201",
        "password": "VocaZ2143@",
        "workspace_name": "VOCAB",
        "portfolio_name": "yQqf87T4aXMF"
    },
    {
        "username": "VOCAB10202",
        "password": "VocaZ2144@",
        "workspace_name": "VOCAB",
        "portfolio_name": "BPFx3XDBi2Tx"
    },
    {
        "username": "VOCAB10203",
        "password": "VocaZ2150@",
        "workspace_name": "VOCAB",
        "portfolio_name": "uzus452dkxlx"
    },
    {
        "username": "VOCAB10204",
        "password": "VocaZ2158@",
        "workspace_name": "VOCAB",
        "portfolio_name": "dj8mRmmz0j4T"
    },
    {
        "username": "VOCAB10205",
        "password": "VocaZ2160@",
        "workspace_name": "VOCAB",
        "portfolio_name": "ghRybTEBqgeY"
    },
    {
        "username": "VOCAB10206",
        "password": "VocaZ2167@",
        "workspace_name": "VOCAB",
        "portfolio_name": "cRJVHoHh0VAn"
    },
    {
        "username": "VOCAB10207",
        "password": "VocaZ2171@",
        "workspace_name": "VOCAB",
        "portfolio_name": "vDWnvGuJgUCa"
    },
    {
        "username": "VOCAB10208",
        "password": "VocaZ2180@",
        "workspace_name": "VOCAB",
        "portfolio_name": "56MwrmxTsdHd"
    },
    {
        "username": "VOCAB10209",
        "password": "VocaZ2183@",
        "workspace_name": "VOCAB",
        "portfolio_name": "hBbp6atDankW"
    },
    {
        "username": "VOCAB10210",
        "password": "VocaZ2188@",
        "workspace_name": "VOCAB",
        "portfolio_name": "o1erMDICo0fL"
    },
    {
        "username": "VOCAB10211",
        "password": "VocaZ2189@",
        "workspace_name": "VOCAB",
        "portfolio_name": "9JgzX6bFARdR"
    },
    {
        "username": "VOCAB10212",
        "password": "VocaZ2195@",
        "workspace_name": "VOCAB",
        "portfolio_name": "fDpgJlxJ1qWD"
    },
    {
        "username": "VOCAB10213",
        "password": "VocaZ2203@",
        "workspace_name": "VOCAB",
        "portfolio_name": "x9vrJCe7JMTo"
    },
    {
        "username": "VOCAB10214",
        "password": "VocaZ2205@",
        "workspace_name": "VOCAB",
        "portfolio_name": "4KBTLxsgVXcQ"
    },
    {
        "username": "VOCAB10215",
        "password": "VocaZ2212@",
        "workspace_name": "VOCAB",
        "portfolio_name": "H1Kv5aMnvlKi"
    },
    {
        "username": "VOCAB10216",
        "password": "VocaZ2216@",
        "workspace_name": "VOCAB",
        "portfolio_name": "vgONPzlpzAgq"
    },
    {
        "username": "VOCAB10217",
        "password": "VocaZ2225@",
        "workspace_name": "VOCAB",
        "portfolio_name": "tGJNc1o9CF0n"
    },
    {
        "username": "VOCAB10218",
        "password": "VocaZ2227@",
        "workspace_name": "VOCAB",
        "portfolio_name": "j7gzEN0nU1vN"
    },
    {
        "username": "VOCAB10219",
        "password": "VocaZ2232@",
        "workspace_name": "VOCAB",
        "portfolio_name": "BQDpdsKSBEYR"
    }
]

def load_existing_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_data_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_users(credentials_list, success_json_filename, failed_json_filename):
    url = "http://127.0.0.1:8001/v1/voc/user-management/?type=authenticate_user"
    
    # Load existing data from the JSON files
    success_data = load_existing_data(success_json_filename)
    failed_data = load_existing_data(failed_json_filename)

    for credentials in credentials_list:
        print(f"Creating user {credentials['username']}...")
        payload = {
            "workspace_name": credentials["workspace_name"],
            "portfolio": credentials["username"],
            "password": credentials["password"],
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
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

# Call the function to create users and save the data
success_json_filename = "created_users.json"
failed_json_filename = "failed_users.json"
create_users(credentials_list, success_json_filename, failed_json_filename)

