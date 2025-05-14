import requests

def get_binance_price():
    try:
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        return float(res["price"])
    except:
        return None

def get_coinbase_price():
    try:
        res = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
        return float(res["data"]["amount"])
    except:
        return None

def get_kraken_price():
    try:
        res = requests.get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD").json()
        return float(res["result"]["XXBTZUSD"]["c"][0])
    except:
        return None

def get_bybit_price():
    try:
        res = requests.get("https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT").json()
        return float(res["result"][0]["last_price"])
    except:
        return None

def get_okx_price():
    try:
        res = requests.get("https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT").json()
        return float(res["data"][0]["last"])
    except:
        return None

def get_all_btc_prices():
    return {
        "binance": get_binance_price(),
        "coinbase": get_coinbase_price(),
        "kraken": get_kraken_price(),
        "bybit": get_bybit_price(),
        "okx": get_okx_price(),
    }
