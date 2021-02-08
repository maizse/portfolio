import requests
import json

response = requests.get("https://official-joke-api.appspot.com/random_joke")
status_code = response.status_code

data = json.loads(response.text)
print(data['setup'])
print(".....")
print(data['punchline'])
