import pytest
import unittest
import requests

from StarShips.starwars import *


class StarWarsTesting(unittest.TestCase):

    starwars = StarWars()

    def test_retrieve_data(self):
        response = requests.get('http://url')
        self.assertTrue(response)

    # def test_list_data(self):
    #     test_list =  StarWars()
    #     assert bool(test_list.)



