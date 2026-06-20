import json
import sys
import requests

# Expects the user to specify as command-line argument the number of Bitcoins
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    # number of Bitcoins
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


# Queries the API for the CoinCap Bitcoin Price Index
YourApiKey = "YOUR_API_KEY_HERE"
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + YourApiKey)
except requests.RequestException:
    sys.exit("")

# to see the json file clearly
# print(json.dumps(response.json(), indent=2))

# to save the json file of our request
jfile = response.json()

# get the price of BitCoin from jfile
try:
    bitcoin_price = float(jfile["data"]["priceUsd"])
except KeyError:
    sys.exit("Sorry! Could't find the data.")


# Outputs the current cost of 𝑛 Bitcoins in USD
amount = n * bitcoin_price
print(f"${amount:,.4f}")