import pymongo as pm
import requests as r
import json
from pprint import pprint
from starwars_insersion import Swapi

class Planets(Swapi):

    def __init__(self):
        super().__init__()
        self.format_planets()


    def format_planets(self):
        self.planets = self.set_category('p-lanets')
        for planet in self.planets:
            resident_ids = self.set_variable_ids(planet, 'residents', collection='characters')
            planet['residents'] = resident_ids

            film_ids = self.set_variable_ids(planet, 'films', collection='films')
            planet['films'] = film_ids



def update_db():

    ss = Planets()
    client = pm.MongoClient()
    db = client['starwars']
    db.planets.drop()
    db.create_collection("planets")
    db.planets.insert_many(ss.planets)
    print('insert complete')



update_db()





