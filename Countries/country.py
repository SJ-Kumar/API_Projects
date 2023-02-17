import requests
import json

# Define the access token and LinkedIn API endpoint
access_token = "your_access_token_here"
endpoint = "https://api.linkedin.com/v2/skills?q=field&isTopSkill=true"

# Define the headers for the API request
headers = {
    "Authorization": f"Bearer {access_token}",
    "X-RestLi-Protocol-Version": "2.0.0"
}

# Make the API request
response = requests.get(endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    skills = json.loads(response.text)["elements"]

    # Loop through each skill and print its name
    for skill in skills:
        print(skill["skill"]["name"])
else:
    print(f"Failed to retrieve skills. Response code: {response.status_code}")
