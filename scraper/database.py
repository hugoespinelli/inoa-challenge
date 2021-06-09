from os import getenv

import pymysql.cursors


HOST = getenv("MYSQL_HOST")
USER = getenv("MYSQL_USER")
PASSWORD = getenv("MYSQL_PASSWORD")
DATABASE = getenv("MYSQL_DATABASE")


def get_connection():
    return pymysql.connect(host=HOST,
                           user=USER,
                           password=PASSWORD,
                           database=DATABASE,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
