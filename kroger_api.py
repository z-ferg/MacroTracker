import requests
import json

# Replace with your actual credentials from the Kroger Developer Portal
client_id = "macrotracker-bbc74svk"
client_secret = "qezGuovxk4WCeEIH-l6K56LlWoH3VutUoP4Gh1Pu"

secur_url = "https://api.kroger.com/v1/connect/oauth2/token"
secur_head = {"Content-Type": "application/x-www-form-urlencoded"}
secur_data = {
    "grant_type": "client_credentials",
    "scope": "product.compact",
}
token_response = requests.post(secur_url, data=secur_data, headers=secur_head, auth=(client_id, client_secret))
access_token = token_response.json()["access_token"]


search_url = "https://api.kroger.com/v1/locations"
search_headers = {"Authorization": f"Bearer {access_token}"}
search_params = {
    "filter.zipCode.near": "24060" # Blacksburg Zipcode
}
search_resp = requests.get(search_url, headers=search_headers, params=search_params)
store_id = search_resp.json()["data"][0]["locationId"]

search_url = "https://api.kroger.com/v1/products"
search_headers = {"Authorization": f"Bearer {access_token}"}
search_params = {
    "filter.term": "milk",
    "filter.locationId": store_id,  # Find this on the Kroger Developers site
    "filter.limit": 1,
}
search_resp = requests.get(search_url, headers=search_headers, params=search_params)
product_upc = search_resp.json()["data"][0]["upc"]