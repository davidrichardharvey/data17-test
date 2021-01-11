import requests
import pymongo
from pprint import pprint

class StarWars:

    def __init__(self):
        self.url = "https://swapi.dev/api/starships/"
        self.conn = pymongo.MongoClient()
        self.db = self.conn["starwars"]
        self.starship_list = self.get_starships()
        self.import_list = self.get_pilots()
        self.import_starships()

    def get_starships(self):
        starships = []
        response = requests.get(self.url)
        if response.status_code == 200:
            result = response.json()
            starships = starships + result["results"]
            while result["next"] is not None:
                response = requests.get(result["next"])
                result = response.json()
                starships = starships + result["results"]
            return starships

    def get_pilots(self):
        final_list = []
        for starship in self.starship_list:
            name_list = []
            for pilot_url in starship["pilots"]:
                response = requests.get(pilot_url)
                name_list.append(response.json()["name"])
            temp_id_list = self.get_pilot_id(name_list)
            starship["pilots"] = (list(temp_id_list[:]))
            final_list.append(starship)
        return final_list

    def get_pilot_id(self, name_list):
        pilot_id_list = []
        for name in name_list:
            characters_id = self.db.characters.find({"name": {"$eq": name}}, {"_id": 1})
            for character_id in characters_id:
                pilot_id_list.append(character_id["_id"])
        return pilot_id_list

    def import_starships(self):
        for starship in self.import_list:
            self.db.starships.insert_one(starship)

    def get_my_starship(self, character_name):
        pilot = self.db.characters.find_one({"name": character_name}, {"name": 1})
        starships = self.db.starships.find({"pilots": pilot["_id"]})
        print(f"{character_name} can pilot the following starship(s): ")
        for starship in starships:
            print(starship["name"], starship["model"])


my_starship = StarWars()
user_input = input("Type in the character name to see which starships they can fly:\n")
my_starship.get_my_starship(user_input)