import requests

def get_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"
    response = requests.get(url).json()
    return response['data'][0]
