import requests

def get_btc_dominance():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url).json()
    return response['data']['market_cap_percentage']['btc']
