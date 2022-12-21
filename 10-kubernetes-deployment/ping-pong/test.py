import requests
import json

host = "http://localhost:9696/response"

event = {"event": "PING"}
request = requests.post(url=host).json()
# request = json.dumps(event)

print(request)