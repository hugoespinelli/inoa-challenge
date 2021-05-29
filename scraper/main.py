from scrap import scrap
from load_tables import load_tables
from first_load import first_load


def main():
    scrap()
    first_load()
    load_tables()


if __name__ == "__main__":
    main()