import json
from django.conf import settings

with open(settings.BASE_DIR / "data/market_prices.json") as f:
    MARKET_DATA = json.load(f)


def get_market_price(crop, market):
    for item in MARKET_DATA:
        if item["crop"] == crop and item["market"] == market:
            return item
    return None