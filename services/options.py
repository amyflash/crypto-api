import requests

def get_btc_options():
    url = "https://eapi.binance.com/eapi/v1/exchangeInfo"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        btc_options = [s for s in data.get('symbols', []) if "BTC" in s.get('symbol', "")]
        return btc_options
    except Exception as e:
        return {"error": f"Failed to fetch BTC options: {str(e)}"}
