from etl.transform import Transform

class Load(Transform):

    def __init__(self):
        super().__init__()
    #     self.create_starships_collection()
    #     self.insert_pilots_into_starships()
    #     self.join_pilots_data()
    #
    # def create_starships_collection(self):
    #     return self.db.create_collection("starships")
    #
    # def insert_pilots_into_starships(self):
    #     return self.db.starships.insert_many({"name": self.starship_ids_dict.keys(), "pilot": self.starship_ids_dict.values()})
    #
    #     # a = self.db.starships.insert_one({"name": self.starship_names_list[0], "pilot": self.pilot_id_dict['Chewbacca']})
    #     # b = self.db.starships.insert_one({"name": self.starship_names_list[0], "pilot": self.pilot_id_dict['Han Solo']})
    #     # c = self.db.starships.insert_one({"name": self.starship_names_list[0], "pilot": self.pilot_id_dict['Lando Calrissian']})
    #     # d = self.db.starships.insert_one({"name": self.starship_names_list[0], "pilot": self.pilot_id_dict['Nien Nunb']})
    #     # e = self.db.starships.insert_one({"name": self.starship_names_list[2], "pilot": self.pilot_id_dict['Darth Vader']})
    #     # f = self.db.starships.insert_one({"name": self.starship_names_list[1], "pilot": self.pilot_id_dict['Luke Skywalker']})
    #     # g = self.db.starships.insert_one({"name": self.starship_names_list[1], "pilot": self.pilot_id_dict['Biggs Darklighter']})
    #     # h = self.db.starships.insert_one({"name": self.starship_names_list[1], "pilot": self.pilot_id_dict['Wedge Antilles']})
    #     # i = self.db.starships.insert_one({"name": self.starship_names_list[1], "pilot": self.pilot_id_dict['Jek Tono Porkins']})
    #     #
    #     # return a, b, c, d, e, f, g, h, i
    #
    # def join_pilots_data(self):
    #     return list(self.db.starships.aggregate([{"$lookup": {"from": "characters", "localField": "pilot", "foreignField": "_id", "as": "matched_pilot"}}, {"$project": {"name": 1, "model": 1, "matched_pilot.name": 1}}]))
    #
    #
