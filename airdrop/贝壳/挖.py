import requests
import json


# Function to read tokens from token.txt
def read_tokens(filename="token.txt"):
    with open(filename, "r") as file:
        tokens = file.readlines()
    return [token.strip() for token in tokens]  # Remove any leading/trailing whitespace


# HTTP headers for the request
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://shellscoin.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://shellscoin.com/h5/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/133.0.0.0"
}

# API endpoint for mining
url = "https://shellscoin.com/api/mining/mining"

# Read tokens from token.txt
tokens = read_tokens()

# Loop through each token and send a request
for token in tokens:
    # Update the headers and data with the current token
    headers["token"] = token
    data = {
        "token": token,
        "lang": "zh-tw"
    }

    # Convert the data dictionary to a JSON string
    data_json = json.dumps(data, separators=(',', ':'))

    # Send the POST request
    response = requests.post(url, headers=headers, data=data_json)

    # Print the response from the server
    print(f"Token: {token}")
    print("Response:", response.text)
    print("Status Code:", response.status_code)
    print("-" * 50)