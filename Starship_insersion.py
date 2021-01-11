import pymongo as pm
import requests as r
import json
from pprint import pprint
from starwars_insersion import Swapi

class Starships(Swapi):

    def __init__(self):
        super().__init__()
        self.format_starships()



    def format_starships(self):
        self.starships = self.set_category('starships')
        for starship in self.starships:
            pilot_ids = self.set_variable_ids(starship, "pilots", collection='characters')
            starship['pilots'] = pilot_ids







def update_db():

    ss = Starships()
    client = pm.MongoClient()
    db = client['starwars']
    db.starships.drop()
    db.create_collection("starships")
    db.starships.insert_many(ss.starships)
    print('insert complete')



update_db()