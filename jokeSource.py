import requests
response = requests.get("https://official-joke-api.appspot.com/random_joke")
print(response.status_code)
print(f"Setup: {response.json()['setup']}")
print(f"Punchline: {response.json()['punchline']}")