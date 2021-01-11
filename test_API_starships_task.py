import unittest

# Need function for pagination and saving to json
from API_starships_task import Starship_pilot_scraper
#These tests serve to check that the initial acquisition of the ship list has been successful

class TestShipScraper(unittest.TestCase):


    def test_list_init(self):
        scraper_test = Starship_pilot_scraper()
        #assert that the list is empty on initialisation
        assert bool(scraper_test.ship_list) is False

    def test_list_len(self):
        scraper_test = Starship_pilot_scraper()
        #test the length of the list is correct after the function
        scraper_test.ship_saver()
        assert len(scraper_test.ship_list) == 36

    def test_first_item(self):
        scraper_test = Starship_pilot_scraper()
        #the first vessel in the list is a CR90 corvette
        scraper_test.ship_saver()
        assert scraper_test.ship_list[0]["name"] == "CR90 corvette"

