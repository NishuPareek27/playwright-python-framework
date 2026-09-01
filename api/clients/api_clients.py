import requests
from api.endpoints import BASE_URL


class APIClient:

    def get(self, BASE_URL):
        return requests.get(BASE_URL)


    def post(self, BASE_URL, data=None):
        return requests.post(BASE_URL, data=data)