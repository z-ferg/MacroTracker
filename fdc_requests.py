import requests

food_query = "Mayonnaise"

req = requests.get(
    'https://api.nal.usda.gov/fdc/v1/foods/search', 
    params={
        "api_key": "4rHvJdS0tHznmCfOcJQOgaOBtVwioZluNmctvAbw",
        "query": food_query,
        "pageSize": 5,
    })

foods_list = list(req.json()["foods"])

for food in foods_list:
    print(food["description"])