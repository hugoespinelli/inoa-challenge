import json

import requests
from bs4 import BeautifulSoup

from data_cleaning import DataCleaner
from utils import generate_stock_filename


URL_STOCK_WEBISTE = "https://valorinveste.globo.com/cotacoes/"


def exclude_header_and_footer(rows):
    return rows[1:-1]


def create_stock(data):
    data_text = [d.text for d in data[:-2]]
    return {
        "name": DataCleaner.remove_empty_space(data_text[0]),
        "code": DataCleaner.remove_empty_space(data_text[1]),
        "price": DataCleaner.transform_str_to_int(data_text[2]),
    }


def save_json(data):
    filename = generate_stock_filename()
    with open(filename, 'w') as f:
        json.dump(data, f)


def scrap():

    try:
        print(f"Scrapping {URL_STOCK_WEBISTE}...")
        page = requests.get(URL_STOCK_WEBISTE)
        soup = BeautifulSoup(page.text, 'html.parser')

        print(f"Performing cleaning on data...")
        rows = soup.find_all('tr')
        rows = exclude_header_and_footer(rows)

        stocks = []

        for row in rows:
            data = row.find_all('td')
            stocks.append(create_stock(data))

        print(f"Saving {len(stocks)} stocks information...")
        save_json(stocks)

        print("Scrap ended successfully!")
    except Exception as e:
        print(f"Something goes wrong: {e}. Scrap interrupted!")

scrap()
