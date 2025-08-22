import requests
from thefuzz import fuzz

food_query = "Sweet Baby Rays"

URL_INSTANT = "https://trackapi.nutritionix.com/v2/search/instant"
URL_ITEM = "https://trackapi.nutritionix.com/v2/search/item"

headers = {
    "x-app-id": "cce807dc",
    "x-app-key": "ec25f7291edc2fb718f639f69f942e05",
}

response = requests.get(url=URL_INSTANT, headers=headers, params={"query": food_query})
response.raise_for_status()
instant_data = response.json()

all_items = dict()

for item in instant_data.get("branded"):
    name = item["brand_name_item_name"]
    score = fuzz.ratio(name, food_query) + 10
    all_items[score] = (name, "branded", item["nix_item_id"])
    print(item)
    print()

print("-------------------------------------")

for item in instant_data.get("common"):
    name = item["food_name"]
    score = fuzz.ratio(name, food_query)
    all_items[score] = (name, "common", None)
    print(item)
    print()

best_score, best_item_body = max(all_items.items())
item_name, item_type, nix_item_id = best_item_body

resp = requests.get(URL_ITEM, headers=headers, params={"nix_item_id": nix_item_id})
resp.raise_for_status()
item_data = resp.json()

print("\n--- ITEM DETAILS ---")
print(f"Name: {item_data['foods'][0]['food_name']}")
print(f"Serving Qty: {item_data['foods'][0]['serving_qty']}")
print(f"Serving Unit: {item_data['foods'][0]['serving_unit']}")
print(f"Serving Weight (g): {item_data['foods'][0].get('serving_weight_grams')}")
print(f"Calories: {item_data['foods'][0]['nf_calories']}")