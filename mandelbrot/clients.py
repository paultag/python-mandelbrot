import json


def requests(url):
    import requests
    return requests.get(url).json()


def aiohttp(url):
    import aiohttp
    response = yield from aiohttp.request('GET', url)
    return json.loads((yield from response.read()).decode('utf-8'))
