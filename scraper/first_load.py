import pymysql.cursors

from utils import load_stocks_from_file


def insert_stocks(cursor, stocks):
    sql = "INSERT INTO `stock` (`name`, `code`) VALUES (%s, %s)"
    stocks_names_codes = [tuple(s.values())[:-1] for s in stocks]
    cursor.executemany(sql, stocks_names_codes)


def should_first_load(cursor):
    sql = "SELECT * FROM `stock`"
    cursor.execute(sql)
    return len(list(cursor)) == 0


def first_load():

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='user',
                                password='password',
                                database='stock',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:

            print("Starting first load...")

            if should_first_load(cursor):
                print("Database is empty! Inserting first load...")
                stocks_scraped = load_stocks_from_file()
                insert_stocks(cursor, stocks_scraped)
            else:
                print("Database already sync!...")
               
        connection.commit()

  