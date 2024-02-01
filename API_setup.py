import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"


class IssApi:
    def __init__(self):
        self.longitude = None
        self.response = None
        self.data = None
        self.latitude = None
        self.data_lst = []

    def generate(self):
        self.response = requests.get(url=ISS_URL)
        self.response.raise_for_status()
        self.data = self.response.json()
        iss_position = self.data["iss_position"]
        self.longitude = iss_position["longitude"]
        self.latitude = iss_position["latitude"]
        self.data_lst = [self.longitude, self.latitude, iss_position, self.data]
        return self.data_lst
