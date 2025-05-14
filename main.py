from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.btc_dominance import get_btc_dominance
from services.fear_greed import get_fear_and_greed_index
from services.options import get_btc_options
from services.prices import get_all_btc_prices

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/btc-dominance")
def btc_dominance():
    return {"btc_dominance": get_btc_dominance()}

@app.get("/fear-greed")
def fear_greed():
    return get_fear_and_greed_index()

@app.get("/btc-options")
def btc_options():
    return get_btc_options()

@app.get("/btc-prices")
def btc_prices():
    return get_all_btc_prices()
