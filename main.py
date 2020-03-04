"""
Code that takes the results of PokemonAPI and links
with their official images and generates a JSON file
"""
import json
import requests

POKEMONS = []

ITERATOR = 1

while True:
    RS_POKEMON = requests.get(f"https://pokeapi.co/api/v2/pokemon/{ITERATOR}")

    if RS_POKEMON.status_code != 200:
        print("No more pokemons!")
        break

    POKEMON = RS_POKEMON.json()

    P_ID = str(POKEMON["id"]).zfill(3)
    P_NAME = POKEMON["name"]

    POKEMONS.append(
        {
            "id": P_ID,
            "name": P_NAME,
            "image_hq": f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{P_ID}.png",
            "image": f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{P_ID}.png",
        }
    )

    print(f"id:{P_ID} name:{P_NAME} succefully added!")
    ITERATOR += 1


with open("pokemons.json", "w") as outfile:
    json.dump(POKEMONS, outfile, indent=2)
