from etl.load import Load
from pprint import pprint

starship_collection = Load()

pprint(starship_collection.starship_names_list)
pprint(starship_collection.pilot_names_list)
pprint(starship_collection.pilot_object_ids)
pprint(starship_collection.pilot_id_dict)
pprint(starship_collection.starship_names_dict())
pprint(starship_collection.starship_ids_dict)
pprint(starship_collection.join_pilots_data())

