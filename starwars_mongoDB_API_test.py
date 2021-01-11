from starwars_mongoDB_API import StarWars
import unittest

class TestInitialisation(unittest.TestCase):

    starship = StarWars()

    def test_initialisation(self):
        self.assertTrue(self.starship)
        self.assertTrue(self.starship.db)
        self.assertTrue(self.import_list)

    def test_get_starship(self):
        self.starship.get_starships()
        self.assertTrue(self.starship.starship_list)
        self.assertEqual(len(self.starship.starship_list), 36)

    def test_get_pilots(self):
        self.starship.get_pilots()
        self.assertEqual(len(self.starship.pilot_list), 21)

    # def test_get_my_starship(self):
    #     self.starship.get_my_starship("Luke Skywalker")
    #     self.assertEqual(self.starship.get_my_starship("Luke Skywalker"), "Luke Skywalker")
    #     pass
    #
    # def test_get_pilot_id(self):
    #     self.test_get_pilot_id()

