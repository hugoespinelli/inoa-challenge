import pymysql.cursors
import json

from utils import load_stocks_from_file


def get_stocks_registered(cursor, stock_list):
    sql = "SELECT `id`, `name` FROM `stock` WHERE `name` in ({})".format(format_placeholders())
    cursor.execute(sql, stock_list)
    return list(cursor)


def format_placeholders(placeholders):
    return ", ".join(["%s"] * len(placeholders))



def insert_price_stocks(cursor, price_stocks):
    sql = "INSERT INTO `historic_stock` (`id_stock`, `price`) VALUES (%s, %s)"
    cursor.executemany(sql, price_stocks)


def load_tables():

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='user',
                                password='password',
                                database='stock',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:

            stocks_scraped = load_stocks_from_file()
            stocks_registered = get_stocks_registered(cursor, stocks_scraped)
            prices_to_be_inserted = []

            stocks_registered_indexed_by_code = {s["code"]: s for s in stocks_registered}

            for stock in stocks_scraped:

                code = stock["code"]

                if code in stocks_registered_indexed_by_code:
                    prices_to_be_inserted.append(
                        (stocks_registered_indexed_by_code[code]["id"], stock["price"])
                    )

            # Create a new record
            insert_price_stocks(cursor, prices_to_be_inserted)

        connection.commit()



