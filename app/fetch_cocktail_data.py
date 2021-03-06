import json
import requests

url = 'http://mixopedia.me/api/ingredient'
ingredients = requests.get(url).json()
for i in range(len(ingredients)):
    r = requests.get(url + '/' + str(ingredients[i]['id'])).json()[0]
    ingredients[i]['numberOfCocktails'] = r['numberOfCocktails']
    with open("mixopedia.out", "w") as outfile:
        json.dump(ingredients, outfile, indent=4)
