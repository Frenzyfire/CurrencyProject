import urllib3
import json

http = urllib3.PoolManager()
currency = http.request('GET','https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c')

currency_dict = currency.data.decode('UTF-8'))
print(currency_dict)
for rate in currency:
    print(rate['rates']['GBP])