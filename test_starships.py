from starships import PullData
import unittest

class TestStarship(unittest.TestCase):

    data = PullData()

    def test_dict(self):
        # Test that calls api function returns a non-empty list
        api_list = self.data.starships
        self.assertIsInstance(api_list, list)
        self.assertTrue(api_list)


    def test_create_collection(self, collection_name):
        # Test that checks that a collection has been created
        collections_list = db.get_collection_names()
        self.assertIn(self, collection_name, collections_list)



