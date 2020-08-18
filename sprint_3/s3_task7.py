import requests

def  get_request(url):
    return (lambda **kwargs : requests.get(url = url, params = kwargs).json())
