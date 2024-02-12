import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '32b9f7e7d860d8f261d204ed650c0b43'}

def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers', params = {'level' : 1}, timeout = 5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_id():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : 223}, timeout = 5)
    assert response.json()['trainer_name'] == 'Viktor'