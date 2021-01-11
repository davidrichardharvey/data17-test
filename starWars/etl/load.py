from etl.transform import Transform


class Load(Transform):

    def __init__(self):
        super().__init__()
        self.create_starships_collection()
        self.insert_pilots_into_starships()
        self.join_pilots_data()

    def create_starships_collection(self):
        return self.db.create_collection("starships")

    def insert_pilots_into_starships(self):
        return self.db.starships.insert_many({"name": self.starship_ids_dict.keys(), "pilot": self.starship_ids_dict.values()})

    def join_pilots_data(self):
        return list(self.db.starships.aggregate([{"$lookup": {"from": "characters", "localField": "pilot", "foreignField": "_id", "as": "matched_pilot"}}, {"$project": {"name": 1, "model": 1, "matched_pilot.name": 1}}]))


