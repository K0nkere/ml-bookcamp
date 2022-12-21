import requests

event = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg"
}

event2 = {
    "url": "https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg"
}
url = "http://localhost:8080/2015-03-31/functions/function/invocations"
result = requests.post(url=url, json=event2).json()
print(result)