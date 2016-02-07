from .clients import requests, aiohttp
import os


class Directory:
    def __init__(self, host, client=requests):
        self.host = host
        self.client = client

    def _request(self, path):
        return self.client("{}{}".format(self.host, path))

    def experts(self):
        return self._request("/api/experts/")

    def expert(self, id):
        return self._request("/api/expert/{}/".format(id))


directory = Directory("http://localhost:8000")
aiodirectory = Directory("http://localhost:8000", client=aiohttp)
