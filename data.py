import requests
import json

r = requests.get('https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c')
data = r.json()

gbp = data["rates"]["GBP"]
eur = data["rates"]["EUR"]
jpy = data["rates"]["JPY"]
sgd = data["rates"]["SGD"]


print('GBP', gbp)
print('EUR', eur)
print('JPY', jpy)
print('SGD', sgd)