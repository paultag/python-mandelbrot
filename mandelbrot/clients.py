import json


def requests(url, auth_username, auth_password, **kwargs):
    import requests

    rqkwargs = {}
    if auth_username is not None:
        rqkwargs['auth'] = requests.auth.HTTPBasicAuth(auth_username, auth_password)
    return requests.get(url, **rqkwargs).json()


def aiohttp(url, auth_username, auth_password, **kwargs):
    import aiohttp

    rqkwargs = {}
    if auth_username is not None:
        rqkwargs['auth'] = aiohttp.BasicAuth(auth_username, auth_password)

    response = yield from aiohttp.request('GET', url, **rqkwargs)
    return json.loads((yield from response.read()).decode('utf-8'))
