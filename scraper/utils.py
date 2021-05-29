import json
from datetime import datetime, timezone

STOCK_FILENAME = "data/stock-{date}.json"


def generate_stock_filename():
    return STOCK_FILENAME.format(
        date=datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    )


def load_stocks_from_file():
    with open(generate_stock_filename()) as json_file:
        return json.load(json_file)