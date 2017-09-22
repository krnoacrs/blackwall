"""
Obsolete implementation
Now using krakenex python lib
"""

import time
import requests
import json
import sys
import os
import time

# Function to load the API key (key+secret)
def load_key(path):
        with open(path, 'r') as f:
                key = f.readline().strip()
                secret = f.readline().strip()
        return [key, secret]

# Function to check the response received from the API
def check_response(response):
	if (response.status_code == 200):
		str = "Connected okay"
	elif (response.status_code == 301):
		str = "Redirected to a different endpoint"
	elif (response.status_code == 401):
		str = "Not authenticated"
	elif (response.status_code == 400):
		str = "Bad request, some data is wrong in the GET"
	elif (response.status_code == 403):
		str = "Forbidden, you have no permissons"
	elif (response.status_code == 404):
		str = "Resource is not found"
	else:
		sys.exit(1)
	return str

# Function to print the JSON whether is DICT or STR
def print_json(json_obj, sort=False, indents=4):
    if type(json_obj) is str:
        print(json.dumps(json.loads(json_obj), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_obj, sort_keys=sort, indent=indents))
    return None



# Key loading
load_key('C:\\Users\\cristian\\work\\repositories\\keys\\laptop_kraken.key')


# Kraken wide variables
kraken_api="https://api.kraken.com/"
kraken_api_version="0/"

# Public URLs no need for key/secret combination
kraken_asset_info_url = kraken_api+kraken_api_version+"public/Assets"
kraken_server_time_url = kraken_api+kraken_api_version+"public/Time"
kraken_tradable_asset_pairs_url = kraken_api+kraken_api_version+"public/AssetPairs"
kraken_ticker_info_url = kraken_api+kraken_api_version+"public/Ticker"
kraken_ohlc_url = kraken_api+kraken_api_version+"public/OHLC"



# Params for what we are interested in XXRP, XXBT, XLTC, ZEUR

parameters = {"pair" : "XXRPZEUR"}
currentMovingAverage = 0
prices = []
lastTrade = 0

timeout = time.time() + 60*60*24
while True:
        response = requests.get(kraken_ticker_info_url, params=parameters)
        check_response(response)
        data = response.json()

        if (len(prices) > 1):
                currentMovingAverage = sum(prices) / float(len(prices))
        
        lastTrade = float(data['result']['XXRPZEUR']['c'][0])
        prices.append(lastTrade)
        print("Kraken - %s - XRP/EUR - last transaction %r | moving average %r" % (check_response(response), lastTrade, currentMovingAverage))

        # could be 10 but don't take any chances
        time.sleep(14)
		if time.time() > timeout:
			break
		


#print (dict(data["XXRP"]))

#print_json(data)

