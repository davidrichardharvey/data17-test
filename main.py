import requests
from pprint import pprint
import json



class Api:
    def __init__(self, category, item):
        self.api_url = 'https://swapi.dev/api/'
        self.category = category
        self.item = item
        self.requested_url = ""
        self.data = ""
        self.data_dict = ""

    def url_setup(self):  # uses the class instantiation arguments to retrieve the correct url
        url = f"https://swapi.dev/api/{self.category}/{self.item}"
        self.requested_url = url
        self.connection_checker()  # Once the URL is setup will then check

    def connection_checker(self):  # If the URL is correct and has a 200 connection, then the puller method runs,
        # else prints error
        db_ping = requests.get(self.requested_url)
        print(db_ping.status_code)
        if db_ping.status_code == 200:
            print("connection successful")
            self.puller()
            list_of_starships.append(self.data_dict)
        else:
            print("Error with connection to database")

    def puller(self):  # url is assigned to the variable for easier reading, the data requested is then retrieved and
        # runs the save method
        url = self.requested_url
        url = requests.get(url).json()
        self.data_dict = url
        self.data = url
        self.data_saver()

    def data_saver(self):
    #  This method creates a new .json file using the name of the document as the filename
        with open(f"{self.data_dict['name']}.json", 'w') as fp:
            json.dump(self.data, fp)
            print("\n  \n  \n")

        # with open('data.json') as json_file:
        #     data = json.load(json_file)
        #     pprint(data)

        # Optional method included to print the files in order to check they were written correctly


i = 0
list_of_starships = []
for i in range(1, 100):
    starship = Api("starships", i)
    starship.url_setup()
pprint((list_of_starships), sort_dicts=False)
print(len(list_of_starships))
# request = Api("starships")
# request.url_setup()
