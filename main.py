"""
Code that links images of pokemon from the official website with their
names and ids and generates a JSON file
"""
import json
import requests

NUM_OF_POKEMONS = 808
POKEMONS = []

for i in range(1, NUM_OF_POKEMONS):
    rs_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    pokemon = rs_pokemon.json()

    p_id = str(pokemon["id"]).zfill(3)
    p_name = pokemon["name"]

    rs_image_high = (
        f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{p_id}.png"
    )
    rs_image_small = (
        f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{p_id}.png"
    )

    POKEMONS.append(
        {
            "id": p_id,
            "name": p_name,
            "image_hq": rs_image_high,
            "image": rs_image_small,
        }
    )

    print(f"id:{p_id} name:{p_name} succefully added!")


with open("pokemons.json", "w") as outfile:
    json.dump(POKEMONS, outfile, indent=2)
