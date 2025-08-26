import requests, json
from thefuzz import fuzz

food_query = "Banana"

URL_INSTANT = "https://trackapi.nutritionix.com/v2/search/instant"
URL_ITEM = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": "cce807dc",
    "x-app-key": "ec25f7291edc2fb718f639f69f942e05",
}

response = requests.get(url=URL_INSTANT, headers=headers, params={"query": food_query})
response.raise_for_status()
top_result_name = response.json()["common"][0]["food_name"]


headers['Content-Type'] = 'application/json'

response = requests.post(url=URL_ITEM, headers=headers, json={"query": top_result_name})
response.raise_for_status()
nutrition_data = response.json()

print(nutrition_data)