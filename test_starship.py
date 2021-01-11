from starships import Starship
import unittest


class StarshipTest(unittest.TestCase):

    star = Starship()

# Test to make sure there is an empty list in the initalisation
    def test_list_empty(self):
        self.assertFalse(self.star.starship_data)

# Test to check that the request for the data from the API has been successful
    def test_request(self):
        self.assertTrue(self.star.request_data())

# Test that the data has been appended to the list
    def test_list_insert(self):
        self.assertTrue(self.star.ship_data_collector())

# Test that the correct number of starships is in the list
    def test_list_len(self):
        self.assertTrue(len(self.star.starship_data) == 36)



