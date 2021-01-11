import pymongo
from pprint import pprint
from main import Api

client = pymongo.MongoClient()

db = client['Starwars']

for pilot in db.characters.find({}, {"name": 1, "_id": 0}):
    pprint(pilot)

for ship in db.starships.find({}, {"pilots": 1, "name": 1, "_id": 0}):
    print(ship)


# class Queries:  # Queries class, trying to decide on its use
#     def __init__(self, category, item, query, filters):
#         super().__init__(category, item)
#         self.query = query
#         self.filters = filters
#
#     def find(self):
#         data = db.characters.find({self.query}, {self.filters})
#         pprint(data)

class Pilots(Api):
    def __init__(self, category, item):
        super().__init__(category, item)

        # url setup method
        # connection checker method
        # puller method


"""
Steps:
9. Access the URL key value for pilots, run it through a similar information puller method
10. store the names of the corresponding pilots with that URL
11. match the starship information and 
12. run the $ lookup and $ project methods to combine the data by ObjectIDs
13. use update() to change the URLs of the starships pilots to the object IDs

"""
