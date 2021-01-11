import requests
import pymongo

# star wars api url
starships_url = "https://swapi.dev/api/starships"

# class to pull info from the api
class Extract:
    # initialisation
    def __init__(self):
        self.starships_data = self.retrieve_starship_info()
        self.retrieve_starships()
        self.retrieve_pilot_urls()
        self.retrieve_pilot_names()
        # initialise pymongo
        self.db = pymongo.MongoClient()['starwars']
        self.pilot_object_ids = self.retrieve_pilot_object_ids()

    # method that pulls the starship data
    def retrieve_starship_info(self):
        r = requests.get(starships_url)
        if r.status_code == 200:
            request = r.json()
            return request["results"]

    # mehthod that retrieves starship names w/ pilots
    def retrieve_starships(self):
        self.starship_names_list = []

        for i in self.starships_data:
            for key, value in i.items():
                if key == "pilots" and len(value) != 0:
                    self.starship_names_list.append(i["name"])

    # create nested list of pilots urls
    def retrieve_pilot_urls(self):
        self.pilot_urls_list = []

        for i in self.starships_data:
            for key, value in i.items():
                if key == "pilots" and len(value) != 0:
                    self.pilot_urls_list.append(value)

    # create nested list of pilot names
    def retrieve_pilot_names(self):
        self.pilot_names_list = self.pilot_urls_list.copy()

        for idx1, item in enumerate(self.pilot_names_list):
            for idx2, url in enumerate(item):
                pilot_r = requests.get(url)
                if pilot_r.status_code == 200:
                    pilot_data = pilot_r.json()
                    self.pilot_names_list[idx1][idx2] = pilot_data["name"]

    # create 2 lists with pilot ids and pilot names
    def retrieve_pilot_object_ids(self):
        self.pilots_list = []

        for pilots in self.pilot_names_list:
            for pilot in pilots:
                self.pilots_list.append(pilot)

        pilot_ids = list(self.db.characters.find({"name": {"$in": self.pilots_list}}, {"_id": 1, "name": 1}))

        for items in pilot_ids:
            for id in items:
                return [items['_id'] for items in pilot_ids], [items["name"] for items in pilot_ids]


