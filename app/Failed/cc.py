import requests
import json

url = "https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c"

response = requests.get(url)

data = response.text

parsed = json.loads(data)

print(parsed)

print(json.dumps(parsed, indent = 3))

#base_rate = parsed["base"]["USD"]
eur_rate = parsed["symbol"]["EUR"]
gbp_rate = parsed["symbol"]["GBP"]

print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(eur_rate) + " EUR")