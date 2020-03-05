# Pokemon images list

Relates PokeAPI results to official images 😊

<p align="center">
<a href="https://github.com/rihor/pokemon-image-list/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Get started

Inside the project run these commands:

```bash
pipenv shell
pipenv sync
python main.py
```

This will generate a `pokemons.json` file.

Each entry on the JSON file will contain:

```json
{
  "id": "001",
  "name": "bulbasaur",
  "image_hq": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png",
  "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/001.png",
  "types": [
    {
      "name": "poison",
      "slot": 2
    },
    {
      "name": "grass",
      "slot": 1
    }
  ]
},
```
