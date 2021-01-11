"""
Pull data on star ships
Pilots key contains URL's that points to characters that pilot that star ships
Use those URLs to pull that data on the character
Use that info to extract the object ID for that pilot
Replace the pilot URL with the object ID as reference

"""
import requests
import json
import pymongo
from pprint import pprint

# url = "https://swapi.dev/api/starships/?page="

# connection to mongodb, making sure we have our mongod running
client = pymongo.MongoClient()
db = client["StarWars"]

class starships:
    def __init__(self):
        self.url = "https://swapi.dev/api/starships/?page="
        # self.r = requests.get(self.url)
        self.meta_list = []
        self.ships = []

        self.get_starships_info()
        self.get_ships_data()


    def get_starships_info(self):
        # can change the while loop, to make it more extensible
        # \\set counter that also works to filter pages and get url for each page and append that as a json to a list
        i = 1
        while i < 5:
            rr = requests.get(self.url + str(i))
        # make sure we get the right status code
            if rr.status_code == 200:
                all_data = rr.json()
                self.meta_list.append(all_data)
                i += 1


    def get_ships_data(self):
        # Using our meta list of pages for the starships
        # we can loop through to append the list of just the ships and their data to a seperate list
        for page in self.meta_list:
            for ship in page["results"]:
                self.ships.append(ship)

    def get_pilots(self):
        # using our previous list, we now go through the list of dictionaries
        # which contain data for each ships, then filter through to get the pilot url for each ship, minus the nulls
        pilots_list = []
        for dict in self.ships:
            for pilots in dict["pilots"]:
                pilots_list.append((dict["name"],pilots))
        return pilots_list

    # method that gets the name of the vehicle and actual name of pilots instead of urls
    def get_pilots_names(self):
        ships_and_pilots_list = []
        pilots_names = []
        for dict in self.ships:
            for pilots in dict["pilots"]:
                # use the pilots url now to retrieve the object data
                pr = requests.get(pilots)
                # check to make sure it works
                if pr.status_code == 200:
                    character = pr.json()
                    # list of ships + pilot names
                    ships_and_pilots_list.append((dict["name"],character["name"]))
                    # list of just the pilot names
                    pilots_names.append(character["name"])
        return ships_and_pilots_list, set(pilots_names)


    # getting the ObjectIds for the characters from our Mongo db
    def get_ObjectIds(self):
        objectIds = []
        han = db.characters.find({"name": "Han Solo"})
        print([(name["name"], name["_id"]) for name in han])






test = starships()

# pprint(len(test.meta_list))
# test.get_ships_data()
# pprint(len(test.ships))

# pprint(test.get_pilots2())

# pprint(test.get_pilots_names())

pprint(test.get_ObjectIds())






