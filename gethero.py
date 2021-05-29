from config import API_KEY, API_HOST
from logging import error
from werkzeug.exceptions import HTTPException
import requests
from requests import exceptions

url = "https://superhero-search.p.rapidapi.com/api/"

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': API_HOST
    }
def get_super_byName(hero):
    try:
        querystring = {"hero": hero}    
        response = requests.request("GET", url, headers=headers, params=querystring).json()

        return response
    except exceptions.ConnectionError:
        print('Not connected')
        return error(404)