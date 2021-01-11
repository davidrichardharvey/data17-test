#Import of all relevant modules
import pymongo
import requests


#note: there are 36 ships in the collection

class Starship_pilot_scraper:
    #initialise all key variables and the empty list of ships
    def __init__(self):
        self.url = "https://swapi.dev/api/starships/"
        try:
            self.r = requests.get(self.url)
        except:
            print("There was an error connecting to the server.")
        self.data = self.r.json()
        self.ship_list = []
        self.client = pymongo.MongoClient()
        self.db = self.client["starwars"]


    def ship_saver(self):
        #loops through the pages of ships and saves their data to a list
        for ship in self.data["results"]:
            self.ship_list.append(ship)
        #additional for-loop necessary for grabbing first page
        while self.data["next"] is not None:
            url = self.data["next"]
            r = requests.get(url)
            if r.status_code == 200:
                self.data = r.json()
                for ship in self.data["results"]:
                    #The entire dataset is appended to the list
                    self.ship_list.append(ship)

    def find_pilots(self):
        #Function to get pilots URLs
        for ship in self.ship_list:
            #unncessary information is popped from the list
            ship.pop("created")
            ship.pop("edited")
            ship.pop("url")
            pilot_names = self.find_names(ship["pilots"])
            pilot_ids = self.find_char_ids(pilot_names)
            ship["pilots"] = pilot_ids

    def find_names(self, pilot_urls):
        #Function to get a pilot's name from a URL
        pilot_names = []
        for pilot in pilot_urls:
            url = pilot
            r = requests.get(url)
            data = r.json()
            pilot_names.append(data["name"])
        return pilot_names

    def find_char_ids(self, pilot_names):
        #Function to use the acquired pilot names to run a search for object IDs
        pilot_ids = []
        for pName in pilot_names:
            character = self.db.characters.find_one({"name": pName}, {"_id": 1})
            pilot_ids.append(character["_id"])
        return pilot_ids

    def update_db(self):
        self.db.starships.drop()
        #Drop the collection first to avoid possible duplicates
        self.db.create_collection("starships")
        self.db.starships.insert_many(self.ship_list)

get_ships = Starship_pilot_scraper()
get_ships.ship_saver()
get_ships.find_pilots()
get_ships.update_db()
