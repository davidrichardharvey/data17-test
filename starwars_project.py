#PLAN
"""
Tasks:
Write tests for all functions

Create collection of starships in starwars database
get starship data from swapi.dev
use pilot to reference character in api
find character in characters collection
get objectID's of pilots and replace url ref's with objectID ref's



Method:
Write function to get api data
function to create starship collection and add data
function to get url's for characters from pilot field and assign to pilot name
function to search characters collection for pilots and get ObjectID's
function to update starship collection with objectID ref's

"""
#import modules
import pymongo
import json
import requests
from pprint import pprint
client = pymongo.MongoClient()
db = client["starwars"]

class StarShip():
    def __init__(self):
        self.ship_ref = "https://swapi.dev/api/starships/" #base url for all ship data
        self.ship_data = None
    def get_starship_data(self, number): #requests data from url, then if the url returns valid data, adds to ship_data
        get_data = requests.get(f"{self.ship_ref}{number}/")
        data = get_data.json()
        if data != {'detail': 'Not found'}:
            self.ship_data = data
    def _get_pilot_names(self, ship_data): #finds pilot names from list
        url = ship_data["pilots"]
        pilot_names = [requests.get(pilot).json()["name"] for pilot in url]
        return pilot_names
    def get_pilot_ids(self, ship_data): #finds objectID's for pilots with names in pilot_names
        pilot_names = self._get_pilot_names(ship_data)
        pilot_ids = []
        for name in pilot_names:
            pilot_ids.append(db.characters.find_one({"name": name}, {"_id": 1})["_id"])
        return pilot_ids
    def update_ship_entry(self, ship_data, category, category_data): #sets pilot field of ship data to be pilotID's not url's
        ship_data[category] = category_data
        return ship_data
    def add_to_collection(self, ship_data): #adds updated ship entry to collection
        db.starship_test.insert_one(ship_data)



db.starship_test.drop()
