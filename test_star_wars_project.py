"""
Pull data on star ships
Pilots key contains URL's that points to characters that pilot that star ships
Use those URLs to pull that data on the character
Use that info to extract the object ID for that pilot
Replace the pilot URL with the object ID as reference

"""


import unittest
import requests
import json
from star_wars_project import starships


class testStarships(unittest.TestCase):

    def test_starships_data_pulled(self):
        # Assume
        shipstest = starships()
        test_l = []

        #Action
        shipstest.get_starships_info(test_l)

        #Assert
        assert bool(test_l) is True













"""

        # data_list = []
        # sships_data = self.r
        # if sships_data.status_code == 200:
        #     data_list.append(sships_data.json())
        # return data_list

    # def get_starship_info(self):
    #     data_list =[]
    #     if self.r == 200:
    #         ships_info = self.r.json()
    #         return ships_info
    #     #     data_list.append(ships_info)
    #     # return data_list


    # def create_ships_list(self):
    #     while self.data["next"]:
    #         url = self.data["next"]
    #         r2 = requests.get(url)
    #         if r2.status_code == 200:
    #             data = r2.json()
    #             for ship in data["results"]:
    #                 self.ships.append(ship)


"""
