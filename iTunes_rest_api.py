import requests
import json

parameters = {"term": "The National", "limit": 5}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)
print(iTunes_response.url)
py_data = json.loads(iTunes_response.text)

for r in py_data['results']:
    print(r['trackName'])


