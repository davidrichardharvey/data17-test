import requests
import pymongo
api_url_starships = "https://swapi.dev/api/starships/"
client = pymongo.MongoClient()
db = client['starwars']


class PullData:

    def __init__(self):
        self.starships = []
        self.get_starships()
        self.get_pilots()
        Transform(self.starships)
        Load(self.starships)


    def get_starships(self):
        # pull data from api on starships
        starships_req = requests.get(api_url_starships)
        starships_dict = starships_req.json()
        self.starships.append(starships_dict)
        while starships_dict['next']:
            req = requests.get(starships_dict['next'])
            starships_dict = req.json()
            self.starships.append(starships_dict)

        return self.starships

    def get_pilots(self):
        # iterate through pilot urls, pull names replace url with name. Do same for films.
        for n in range(len(self.starships)):
            for ship in self.starships[n]['results']:
                pilots = ship['pilots']
                films = ship['films']
                if pilots:
                    pilot_names = []
                    for url in pilots:
                        pilot_req = requests.get(url)
                        pilot = pilot_req.json()
                        pilot_names.append(pilot['name'])
                    ship['pilots'] = pilot_names
                if films:
                    film_names = []
                    for url in films:
                        film_req = requests.get(url)
                        film = film_req.json()
                        film_names.append(film['title'])
                    ship['films'] = film_names


class Transform:

    def __init__(self, extracted_data):
        self.get_ids(extracted_data)

    def get_ids(self, starships):
        # replace pilot names with ids from characters db
        for n in range(len(starships)):
            for ship in starships[n]['results']:
                pilots = ship['pilots']
                if pilots:
                    pilot_ids = []
                    for pilot in pilots:
                        pilot_ids.append(db.characters.find({"name": pilot}, {"_id": 1}).next()['_id'])
                    ship['pilots'] = pilot_ids

class Load():

    def __init__(self, transformed_data):
        self.create_collection()
        self.insert_data(transformed_data)

    def create_collection(self):
        # create starships collection
        col = db["starships"]
        print(db.list_collection_names())

    def insert_data(self, starships):
        # loop through data inserting into starships
        for n in range(len(starships)):
            for ship in starships[n]['results']:
                db.starships.insert_one(ship)





