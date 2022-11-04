import json
import ndjson
import requests
from click import clear

clear()
def getCats():
    # Creates the JSON from the api call
    api_endpoint = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": 'live_6kMXsT3V1srBAcd0KQyCiGEYZYGdjDyOB7kk5E12eAZGBp0cGTfG4xm8J0sXwoa7'
    }
    response = requests.get(
        api_endpoint,
        headers=headers
    )
    cats = response.json(cls=ndjson.Decoder)
    return cats

# def getCatFacts():
#
#     url = 'https://catfact.ninja/fact?max_length=140'
#
#     getResponse = requests.get(url).json()
#     catFactsJson = []
#
#     for jsonObj in getResponse:
#         catFactsDict = json.loads(jsonObj)
#         catFactsJson.append(catFactsDict)
#     return catFactsJson