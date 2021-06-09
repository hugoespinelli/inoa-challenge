import pymysql.cursors

from utils import load_stocks_from_file
from database import get_connection


def get_stocks_registered(cursor, stock_list):
    codes = [s["code"] for s in stock_list]
    sql = "SELECT `id`, `code` FROM `stock` WHERE `code` in ({})".format(format_placeholders(codes))
    cursor.execute(sql, codes)
    return list(cursor)


def format_placeholders(placeholders):
    return ", ".join(["%s"] * len(placeholders))


def insert_price_stocks(cursor, price_stocks):
    sql = "INSERT INTO `historic_stock` (`id_stock`, `price`) VALUES (%s, %s)"
    cursor.executemany(sql, price_stocks)


def load_tables():

    print("Starting load prices process...")

    # Connect to the database
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:

            stocks_scraped = load_stocks_from_file()
            print("Searching stocks registered...")
            stocks_registered = get_stocks_registered(cursor, stocks_scraped)
            prices_to_be_inserted = []
            stocks_registered_indexed_by_code = {s["code"]: s for s in stocks_registered}

            for stock in stocks_scraped:

                code = stock["code"]

                if code in stocks_registered_indexed_by_code:
                    prices_to_be_inserted.append(
                        (stocks_registered_indexed_by_code[code]["id"], stock["price"])
                    )

            print(f"Inserting new {len(prices_to_be_inserted)} stocks prices...")
            insert_price_stocks(cursor, prices_to_be_inserted)

        connection.commit()
