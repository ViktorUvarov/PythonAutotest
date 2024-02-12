import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '32b9f7e7d860d8f261d204ed650c0b43'}
body = {
    "name" : "generate",
    "photo" : "generate"
}
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json = body)
print(f'Статус код: {response.status_code}. Сообщение : {response.json()["message"]}')

body1 = {
    "pokemon_id": "286",
    "name": "282",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body1)
print(f'Статус код : {response.status_code}. Сообщение : {response.json()["message"]}')

body2 = {
    "pokemon_id": "286"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body2)
print(f'Статус код : {response.status_code}. Сообщение : {response.json()["message"]}')