import requests, json
from thefuzz import fuzz

URL_INSTANT = "https://trackapi.nutritionix.com/v2/search/instant"
URL_ITEM = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": "cce807dc",
    "x-app-key": "ec25f7291edc2fb718f639f69f942e05",
}

def make_item_request(food_query):
    response = requests.get(url=URL_INSTANT, headers=headers, params={"query": food_query})
    response.raise_for_status()
    top_result_name = response.json()["common"][0]["food_name"]


    headers['Content-Type'] = 'application/json'

    response = requests.post(url=URL_ITEM, headers=headers, json={"query": top_result_name})
    response.raise_for_status()
    d = response.json()["foods"][0]
    
    d.pop("full_nutrients")
    d.pop("alt_measures")
    d.pop("tags")
    d.pop("photo")
    d.pop("metadata")
    
    return api_ingredient(name=d["food_name"], s_qty=d["serving_qty"], s_unit=d["serving_unit"],
                        grams=d["serving_weight_grams"],
                        cals=d["nf_calories"],
                        tot_fat=d["nf_total_fat"],
                        sat_fat=d["nf_saturated_fat"],
                        tra_fat=0,
                        chol=d["nf_cholesterol"],
                        sod=d["nf_sodium"],
                        carbs=d["nf_total_carbohydrate"],
                        fiber=d["nf_dietary_fiber"],
                        sugars=d["nf_sugars"],
                        add_sugars=0,
                        protein=d["nf_protein"],
                        )

class api_ingredient():
    def __init__ (self, name, s_qty=0, s_unit="None", grams=0, cals=0, tot_fat=0, sat_fat=0,
                tra_fat = 0, chol=0, sod=0, carbs=0, fiber=0, sugars=0, add_sugars=0, protein=0):
        self.name = name
        self.s_qty = s_qty
        self.s_unit = s_unit
        self.grams = grams
        self.cals = cals
        self.tot_fat = tot_fat
        self.sat_fat = sat_fat
        self.tra_fat = tra_fat
        self.chol = chol
        self.sod = sod
        self.carbs = carbs
        self.fiber = fiber
        self.sugars = sugars
        self.add_sugars = add_sugars
        self.protein = protein
    
    def __str__ (self):
        s = ""
        s += f'Item Name: \t\t{self.name}\n'
        s += f'Serving Size: \t\t{self.s_qty}\n'
        s += f'Serving Unit: \t\t{self.s_unit}\n'
        s += f'Serving Weight: \t\t{self.grams}g\n'
        s += f'Calories: \t\t{self.cals}\n'
        s += f'Total Fat: \t\t{self.tot_fat}g\n'
        s += f'Saturated Fat: \t\t{self.sat_fat}g\n'
        s += f'Trans Fat: \t\t{self.tra_fat}g\n'
        s += f'Cholesterol: \t\t{self.chol}mg\n'
        s += f'Sodium: \t\t{self.sod}mg\n'
        s += f'Total Carbs: \t\t{self.carbs}g\n'
        s += f'Fiber: \t\t{self.fiber}g\n'
        s += f'Total Sugars: \t\t{self.sugars}g\n'
        s += f'Added Sugars: \t\t{self.add_sugars}g\n'
        s += f'Protein: \t\t{self.protein}g\n'

        return s

"""
'serving_qty': 1, 
'serving_unit': 'large', 
'serving_weight_grams': 50,
'nf_calories': 71.5, 
'nf_total_fat': 4.76,
'nf_saturated_fat': 1.56, 
'nf_cholesterol': 186, 
'nf_sodium': 71,
'nf_total_carbohydrate': 0.36,
'nf_dietary_fiber': 0, 
'nf_sugars': 0.19, 
'nf_protein': 6.28,
"""