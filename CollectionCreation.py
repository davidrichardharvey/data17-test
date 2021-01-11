from StarShips.starwars import StarWars
import pymongo
client = pymongo.MongoClient()
db = client['StarWars']


class Collection(StarWars):

    def __init__(self):
        super().__init__()
        self.add_new_data()

    def add_new_data(self):
        collection = db.starships.insert_many(self.data)


new = Collection()