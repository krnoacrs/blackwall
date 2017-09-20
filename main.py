
import requests
import json

# Function to check the response received from the API
def check_response(response):
	if (response.status_code == 200):
		print ("Everything went okay")
	elif (response.status_code == 301):
		print ("Redirected to a different endpoint")
	elif (response.status_code == 401):
		print ("Not authenticated")
	elif (response.status_code == 400):
		print ("Bad request, some data is wrong in the GET")
	elif (response.status_code == 403):
		print ("Forbidden, you have no permissons")
	elif (response.status_code == 404):
		print ("Resource is not found")
	else:
		print ("Google it" , response.status.code)
	return None

# Function to print the JSON whether is DICT or STR
def print_json(json_obj, sort=True, indents=4):
    if type(json_obj) is str:
        print(json.dumps(json.loads(json_obj), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_obj, sort_keys=sort, indent=indents))
    return None

# Public URLs no need for key/secret combination
kraken_asset_info_url = "https://api.kraken.com/0/public/Assets"
kraken_server_time_url = "https://api.kraken.com/0/public/Time"
kraken_tradable_asset_pairs_url = "https://api.kraken.com/0/public/AssetPairs"
kraken_ticker_info_url = "https://api.kraken.com/0/public/Ticker"
kraken_ohlc_url = "https://api.kraken.com/0/public/OHLC"


parameters = {"pair" : "XXBTZEUR, XXBTZUSD"}

response = requests.get(kraken_ticker_info_url, params=parameters)

check_response(response)




#data = response.json()

#print_json(data)

