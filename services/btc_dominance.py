import requests

def get_btc_dominance():
    print("Fetching BTC Dominance...")
    url = "https://api.coingecko.com/api/v3/global"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        dominance = data.get("data", {}).get("market_cap_percentage", {}).get("btc", None)
        print("BTC Dominance:", dominance)
        return dominance
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}

if __name__ == "__main__":
    get_btc_dominance()
