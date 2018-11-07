from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import urllib2

def getExchangeRates():
    rates = []
    response = urllib2.urlopen('https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c')
    data = response.read()
    rdata = json.loads(data, parse_float=float)
 
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['EUR'] )
    rates.append( rdata['rates']['SGD'] )
    rates.append( rdata['rates']['RSD'] )
    return rates
 
@app.route('/')
def index():
    rates = getExchangeRates()
    print(rates)

#from urllib.request import urlopen, Request
#url = "https://openexchangerates.org/api/latest.json?app_id=58824ee47b2f4dcc8290c780d9ab9b2c&symbols=GBP"
#request = Request(url)
#response = urlopen(request)
#html = response.read()
