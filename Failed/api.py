import urllib.parse
import requests
import json

main_api= 'https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c'
#currencies = 'GBP'

url = main_api #+ urllib.parse.urlencode({'&symbols=': currencies}) 

json_data = requests.get(url).json()
json_string = json.dumps(datastore)
datastore = json.loads(json_string)

print(datastore['rates']['GBP'])

