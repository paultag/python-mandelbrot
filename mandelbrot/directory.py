from .clients import requests, aiohttp
import os

COMMON_HOST = "http://mandelbrot.pault.ag"


class Directory:
    def __init__(self, host, client=requests, auth_username=None, auth_password=None):
        self.host = host
        self.client = client
        self.auth_username = auth_username
        self.auth_password = auth_password

    def _request(self, path):
        return self.client(
            "{}{}".format(self.host, path),
            self.auth_username,
            self.auth_password,
        )

    def experts(self):
        return self._request("/api/experts/")

    def expert(self, id):
        return self._request("/api/expert/{}/".format(id))


directory = Directory(COMMON_HOST)
aiodirectory = Directory(COMMON_HOST, client=aiohttp)
