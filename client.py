import requests


def get_example():
    r = requests.get('https://httpbin.org/get')
    return r.json()
