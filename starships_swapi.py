import requests
import json
import pymongo
from pprint import pprint

ship_url = "https://swapi.dev/api/starships"

r = requests.get(ship_url)

ships = []

if r.status_code == 200:
    data = r.json()
    for ship in data['results']:
        ships[ship['name']] = ship['pilots']

pprint(r.json())