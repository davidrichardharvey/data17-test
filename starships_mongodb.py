import pymongo
import requests
from pprint import pprint


# url = 'https://swapi.dev/api/starships/'
# clients = pymongo.MongoClient()
# db = clients['StarWards']

#  creating the starship class
class Starship:
    def __init__(self):
        self.url = 'https://swapi.dev/api/starships/'
        self.client = pymongo.MongoClient()
        self.db = self.client['StarWards']
        self.starship = self.get_starships()
        self.pilots = self.get_pilots()
# method to get the starships info from the starwars api
    def get_starships(self):
        starships = []
        response = requests.get(self.url)
        if response.status_code == 200:
            result = response.json()
            starships += result['results']
            while result['next'] is not None:
                response = requests.get(result['next'])
                result = response.json()
                starships += result['results']
            return starships
# method to get a list of just the pilots from the starships dictionary
    def get_pilots(self):
        name_list = []
        for pilots in self.starship:
            if pilots['pilots'] is not None:
                for pilot in pilots['pilots']:
                    name_list.append(pilot)
        print(len(name_list))
        return name_list


# falcon = Starship('milenium falcon')
# print(falcon.starship_list)


ships = Starship()
pprint(ships.get_starships())
pprint(ships.get_pilots())
