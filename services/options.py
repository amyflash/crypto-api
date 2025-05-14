import requests

def get_btc_options():
    print("Fetching BTC Options Info...")
    url = "https://eapi.binance.com/eapi/v1/exchangeInfo"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        # 筛选 underlying 为 BTCUSDT 的期权合约
        btc_options = [
            s for s in data.get("optionSymbols", [])
            if s.get("underlying") == "BTCUSDT"
        ]
        print(f"Found {len(btc_options)} BTC options.")
        return btc_options
    except Exception as e:
        print("Error fetching BTC options:", e)
        return {"error": str(e)}

if __name__ == "__main__":
    result = get_btc_options()
    print("Result:", result)
