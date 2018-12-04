from app import app
import requests
import json

@app.route('/')
def index():
    res = requests.get('https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c')
    #import pdb (debugging purposes)
    #pdb.set_trace()
    res_str = str(res.json())
    return res_str

    




if __name__ == '__main__':
    app.run()
