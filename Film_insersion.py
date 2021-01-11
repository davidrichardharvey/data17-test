import pymongo as pm
import requests as r
import json
from pprint import pprint
from starwars_insersion import Swapi


class Films(Swapi):

    def __init__(self):
        super().__init__()
        self.format_films()


    def format_films(self):
        self.films = self.set_category('films')
        for film in self.films:
            film.pop('vehicles')
            film.pop('starships')
            film.pop('planets')
            film.pop('species')
            film.pop('characters')






def update_db():

    ss = Films()
    client = pm.MongoClient()
    db = client['starwars']
    db.films.drop()
    db.create_collection("films")
    db.films.insert_many(ss.films)
    print('insert complete')

update_db()

