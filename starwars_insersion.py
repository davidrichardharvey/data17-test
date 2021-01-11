import pymongo as pm
import requests as r
import json
from pprint import pprint


class Swapi():

    def __init__(self):
        self.baseurl = "https://swapi.dev/api/"
        self.headers = {'Content-Type': 'application/json'}
        self.db_name = "starwars"
        self.count = 0

    def set_category(self, category):
        things = []
        count = 1
        page = r.get(self.baseurl + category + "/?page=" + str(count), headers=self.headers).json()
        while "next" in page.keys() or "next" == 'null':
            print("page found")
            count += 1
            for item in page["results"]:
                item.pop('created')
                item.pop('edited')
                item.pop('url')
                things.append(item)
                page = r.get(self.baseurl + category + "/?page=" + str(count), headers=self.headers).json()
        return things

    def set_variable_names(self, category_item, variables):
        variable_names = []
        for variable in category_item[variables]:
            if variables == 'films':
                variable_names.append(r.get(variable, headers=self.headers).json()["title"])
            else:
                variable_names.append(r.get(variable, headers=self.headers).json()["name"])
        return variable_names


    def set_variable_ids(self, category_item, variables, collection):
        # client = pm.MongoClient()
        # db = client[self.db_name]
        variable_ids = []
        varibale_names = self.set_variable_names(category_item, variables)
        client = pm.MongoClient()
        db = client[self.db_name]
        for name in varibale_names:
            if self.count % 20 == 0:
                print('\n')
            else:
                print('.', end='')

            if collection == 'characters':
                variable_id = db.characters.find({"name": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)

            elif collection == 'films':
                variable_id = db.films.find({"title": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)

            elif collection == 'planets':
                variable_id = db.planets.find({"name": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)

            elif collection == 'species':
                variable_id = db.species.find({"name": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)

            elif collection == 'vehicles':
                variable_id = db.vehicles.find({"name": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)

            elif collection == 'starships':
                variable_id = db.starships.find({"name": name}, {"_id": 1}).next()["_id"]
                variable_ids.append(variable_id)
            self.count +=1



        return variable_ids
