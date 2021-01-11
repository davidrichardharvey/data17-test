from starwars_project import StarShip
import unittest
import pymongo
import json
from pprint import pprint
client = pymongo.MongoClient()
db = client["starwars"]
db.ships_test_all.drop() #drops collection to avoid duplicats and errors

db.create_collection("ships_test_all") #creates collection to add data to
for i in range(100): #url's are all numbered. this loops through ship urls
    starships = StarShip() #create starship object

    starships.get_starship_data(i) #request data from url
    if starships.ship_data is not None: #if url has valid data
        pilot_data = starships.get_pilot_ids(starships.ship_data) #get pilot id's from data
        pprint(starships.ship_data) #see what data will be added to the collection
        starships.update_ship_entry(starships.ship_data, "pilots", pilot_data) #update ship data to replace pilot url's with object references
        starships.add_to_collection(starships.ship_data) #add updated entry to collection
