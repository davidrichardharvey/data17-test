from etl.extract import Extract

# class that transform data into dictionaries
class Transform(Extract):

    def __init__(self):
        super().__init__()
        self.pilot_id_dict = self.create_pilot_id_dict()
        self.starship_names_dict()
        self.starship_ids_dict = self.create_starship_ids_dict()

    def create_pilot_id_dict(self):
        self.id_strings_list = []

        # convert ids into string
        for i in self.pilot_object_ids[0]:
            self.id_strings_list.append(f'ObjectId("{str(i)}")')

        # create a zip object and convert it to dictionary
        self.zip_pilot_id = zip((self.pilot_object_ids[1]), self.pilot_object_ids[0])
        return dict(self.zip_pilot_id)

    def starship_names_dict(self):
        self.zip_starship_names = zip(self.starship_names_list, self.pilot_names_list)
        return dict(self.zip_starship_names)

    def create_starship_ids_dict(self):
        self.pilot_ids_list = self.pilot_names_list.copy()

        # change pilot names list to ids
        for idx1, names in enumerate(self.pilot_ids_list):
            for idx2, name in enumerate(names):
                self.pilot_ids_list[idx1][idx2] = self.pilot_id_dict[name]

        # create a zip object and convert it to dictionary
        self.zip_starship_ids = zip(self.starship_names_list, self.pilot_ids_list)
        return dict(self.zip_starship_ids)


