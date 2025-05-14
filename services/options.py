import requests

def get_btc_options():
    url = "https://eapi.binance.com/eapi/v1/exchangeInfo"
    response = requests.get(url).json()
    btc_options = [s for s in response['symbols'] if "BTC" in s['symbol']]
    return btc_options
