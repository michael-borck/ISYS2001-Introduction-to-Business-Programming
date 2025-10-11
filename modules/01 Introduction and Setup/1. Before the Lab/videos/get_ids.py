import requests
import json

XI_API_KEY = "sk_4770b8e0f21cd2c49ce946b3f163225b306fe4070d799ecf"  # Replace with your API key
url = "https://api.elevenlabs.io/v1/voices"
headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

for voice in data['voices']:
    print(f"{voice['name']}; {voice['voice_id']}")
