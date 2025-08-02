import requests

def fetch_price_binance():
    try:
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        return float(res.json()["price"])
    except Exception as e:
        print("Binance error:", e)
        return None

def fetch_price_bybit():
    try:
        res = requests.get("https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT")
        data = res.json()
        return float(data["result"]["list"][0]["lastPrice"])
    except Exception as e:
        print("Bybit error:", e)
        return None


def fetch_price_okx():
    try:
        res = requests.get("https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT")
        return float(res.json()["data"][0]["last"])
    except Exception as e:
        print("OKX error:", e)
        return None

def fetch_price_bitget():
    try:
        res = requests.get("https://api.bitget.com/api/spot/v1/market/tickers")
        data = res.json().get("data", [])
        for item in data:
            if item.get("symbol") == "BTCUSDT":
                return float(item["close"])
        print("Bitget BTCUSDT not found in response.")
        return None
    except Exception as e:
        print("Bitget error:", e)
        return None


def fetch_price_upbit():
    try:
        res = requests.get("https://api.upbit.com/v1/ticker?markets=USDT-BTC")
        return float(res.json()[0]["trade_price"])
    except Exception as e:
        print("Upbit error:", e)
        return None

def fetch_price_gate():
    try:
        res = requests.get("https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT")
        data = res.json()
        if isinstance(data, list) and len(data) > 0:
            return float(data[0]["last"])
        print("Gate.io unexpected data:", data)
        return None
    except Exception as e:
        print("Gate error:", e)
        return None


def get_all_prices():
    print("Fetching BTC prices from all exchanges...")
    return {
        #"binance": fetch_price_binance(),
        #"bybit": fetch_price_bybit(),
        "okx": fetch_price_okx(),
        #"bitget": fetch_price_bitget(),
        #"upbit": fetch_price_upbit(),
        #"gate": fetch_price_gate()
    }


if __name__ == "__main__":
    prices = get_all_prices()
    print("BTC Prices:", prices)
