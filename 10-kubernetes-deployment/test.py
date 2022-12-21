import requests
import json

event = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

# url = "http://localhost:9696/predict"
url = "http://localhost:8080/predict"

result = requests.post(url=url, json=event).json()

print(json.dumps(result, indent=2))