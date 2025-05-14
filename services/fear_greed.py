import requests

def get_fear_and_greed():
    print("Fetching Fear & Greed Index...")
    url = "https://api.alternative.me/fng/"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
        value = data.get("data", [])[0].get("value")
        print("Fear & Greed Index:", value)
        return value
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}

if __name__ == "__main__":
    get_fear_and_greed()
