import requests
import json
import base64
import hmac
import hashlib
import datetime, time
import logging
from pandas import pandas as pd
from pprint import pprint as pp

base_url = "https://api.gemini.com/v2"
gemini_api_key = "mykey'"
gemini_api_secret = "xxx".encode()
time = datetime.datetime.now()


headers = {
    'X-GEMINI-APIKEY': gemini_api_key,
    }

response = requests.get(base_url + "/candles/btcusd/15m")
#btc_candle_data = response.json()
btc_candle_data = pd.DataFrame(response.json(), columns =['time','open','high','low','close','volume'])

btc_candle_data['time'] = pd.to_datetime(btc_candle_data['time'], unit='ms')
btc_candle_data.set_index('time', inplace=True)
btc_candle_data.sort_values(by =['time'], inplace = True)
print(btc_candle_data)

open_price =btc_candle_data.open['2021-11-15']

#print("open price is", open_price)

base_url = "https://api.gemini.com/v1"
response = requests.get(base_url + "/pricefeed/btcusd")
prices = response.json()
pp(prices)

current_price = prices[0]['price']
print(current_price)


#def percentage(open_price,current_price):
#    return((float(current_price)-open_price)/abs(open_price))*100.00
#print (percentage)

base_url = "https://api.gemini.com/v2"
response = requests.get(base_url + "/ticker/btcusd")
btc_data = response.json()
x = changes [0]
pp(btc_data)
