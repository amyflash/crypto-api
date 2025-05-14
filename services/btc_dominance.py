import requests

def get_btc_dominance():
    url = "https://api.coingecko.com/api/v3/global"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        return data.get("data", {}).get("market_cap_percentage", {}).get("btc", None)
    except Exception as e:
        return {"error": f"Failed to fetch BTC dominance: {str(e)}"}
