from starwars_project import StarShip
import unittest
import pymongo
import json
import requests


client = pymongo.MongoClient()
db = client["starwars"]
db.starship_test.drop()
db.create_collection("starship_test")
class TestStarShip(unittest.TestCase):

    def test_list_empty(self):
        starship_db = StarShip()
        assert(bool(starship_db.ship_data) is False)
        #print(test)
    def test_get_starship_data(self):
        starship_db = StarShip()
        starship_db.get_starship_data(10)
        assert (bool(starship_db.ship_data) is True)
    def test_get_pilot_ids(self):
        starship_db = StarShip()
        starship_db.get_starship_data(10)
        pilot_ids = starship_db.get_pilot_ids(starship_db.ship_data)
        assert bool(pilot_ids) is True
    def test_update_ship_entry(self):
        starship_db = StarShip()
        starship_db.get_starship_data(10)
        pilot_data = starship_db.get_pilot_ids(starship_db.ship_data)
        starship_db.update_ship_entry(starship_db.ship_data, "pilots", pilot_data)
        assert (starship_db.ship_data["pilots"] == pilot_data)
    def test_add_to_collection(self):
        starship_db = StarShip()
        starship_db.get_starship_data(10)
        pilot_data = starship_db.get_pilot_ids(starship_db.ship_data)
        starship_db.update_ship_entry(starship_db.ship_data, "pilots", pilot_data)
        starship_db.add_to_collection(starship_db.ship_data)
        print(starship_db.ship_data)
        print(db.starship_test.find_one({}))

if __name__=="__main__":
    unittest.main()

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