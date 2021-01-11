# Pull data on star ships
# Pilots key contains URL's that points to characters that pilot that star ships
# Use those URLs to pull that data on the character
# Use that info to extract the object ID for that pilot
# Replace the pilot URL with the object ID as reference
# And then write the starship to a MongoDB collection

# Recommendations
# Do it slowly
# OOP
# Functions at the very least
# TDD


# Methods for:
# Pulling starship from starwars API and put into a json file/dict
# Look at the pilot name from the URL and compare the name with the local host
# For the pilots and local host characters that are the same, replace the URL with the object id
# write the starship into a mongoDB collection

# starship_req = requests.get("https://swapi.dev/api/starships/")
# print(starship_req.content)


import requests
from pprint import pprint


class Starship:
    def __init__(self):
        self.starship_data = []
        self.url = "https://swapi.dev/api/starships/"
        self.data = self.request_data()

    def request_data(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.json()

    def ship_data_collector(self):
        for ship in self.data["results"]:
            self.starship_data.append(ship)
        while self.data["next"] is not None:
            url = self.data["next"]
            r = requests.get(url)
            if r.status_code == 200:
                self.data = r.json()
                for ship in self.data["results"]:
                    self.starship_data.append(ship)


starship = Starship()
print(starship.starship_data)
print(len(starship.starship_data))
