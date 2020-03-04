import requests
import re

def getImgFromBulbapedia(bulbapedia_page, p_id, p_name):  
  pattern = f"cdn.bulbagarden.net\/upload\/[a-zA-Z0-9]*\/[a-zA-Z0-9]*\/{p_id}{p_name}.png"
  result = re.search(pattern, bulbapedia_page)
  if(result != None):
    result = result.group()
  return result

def formatName(name):
  formatted_name = name.capitalize()

  if(name.endswith('-f') or name.endswith('-m')):
    print(formatted_name)
    formatted_name = formatted_name[:-len('-f')]
  
  return formatted_name

pokemons = [] 
iterator = 28

while(True):
  pokemon_result = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(iterator))
  
  if pokemon_result.status_code != 200:
    break

  pokemon = pokemon_result.json()
  p_id = str(pokemon['id']).zfill(3)
  p_name = formatName(pokemon['name'])
  bulbapedia_url = "https://bulbapedia.bulbagarden.net/wiki/File:" + str(p_id) + str(p_name) + ".png"
  print('========')
  print(bulbapedia_url)
  print('========')
  bulbapedia_page = requests.get(bulbapedia_url).text
  
  image_url = getImgFromBulbapedia(bulbapedia_page, p_id, p_name)  
  print(image_url)
  if(image_url == None):
    print('Image not found of Pokemon {i}!'.format(i=iterator))
    break

  image_result = requests.get(f"http://{image_url}")  
  if(image_result.status_code != 200):
    print('Image not found of Pokemon {i}!'.format(i=iterator))
    break

  pokemon['image_url'] = image_url
  pokemons.append(pokemon)
  iterator += 1
  print(f"Pokemon: id = {p_id} name = {p_name} url = {pokemon['image_url']}")
