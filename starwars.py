import pymongo
import json
import requests
import pprint

client = pymongo.MongoClient()
db = client['StarWars']

url = 'https://swapi.dev/api/starships/?page='


class StarWars:

    def __init__(self):
        self.retrieve_data()
        # Pulling data, checking status code,and appending each page to a new list
        self.retrieve_pages()
        #takes the 'results' from each page and puts all the data into one complete list
        self.find_pilot_names()
        #Pulls each pilot url and changes them into the object IDs

    def retrieve_data(self):
        self.list = []
        count = 1
        while count < 5:
            try:
                request = requests.get(url + str(count))
                if request.status_code == 200:
                    r = request.json()
                    self.list.append(r)
                    count += 1
            except requests.exceptions.InvalidSchema as ConnectionError:
                print("The URL connection was unsuccessful")
                break
        return self.list


    def retrieve_pages(self):
        self.data = []
        for page in self.list:
            for ship in page['results']:
                self.data.append(ship)
        return self.data

    def find_pilot_names(self):
        for i in self.data:
            #Iterates through the data and changes the information for a pilot one at a time
            pilot_names = self.change_names(i["pilots"])
            character_names = self.find_character_ids(pilot_names)
            i["pilots"] = character_names
            #reassigns the pilot URL with the object ID found in find_character_ids

    def change_names(self, pilots_url):
        # Makes a get request to change a pilot url into a pilot name and sends it back to find_pilot_name method
        pilot_names = []
        for pilot in pilots_url:
            url = pilot
            r = requests.get(url)
            data = r.json()
            pilot_names.append(data["name"])
        return pilot_names

    def find_character_ids(self, pilot_names):
        # here we change the pilot name to the objectID stored in the characters collection
        pilot_ids = []
        for name in pilot_names:
            character = db.characters.find({"name": name}, {"_id": 1})
            for char in character:
                pilot_ids.append(char["_id"])
        return pilot_ids








# Then update many + change list
# maybe drop collection then remake it



start = StarWars()
