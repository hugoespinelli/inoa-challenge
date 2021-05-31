from datetime import datetime, timezone

from scrap import scrap
from load_tables import load_tables
from first_load import first_load


def main():
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d  %H:%M:%S")
    print(f"Starting scrap and loading tables process at {now} UTC...")
    try:
        scrap()
        first_load()
        load_tables()
        print("Scrap and loading tables process ended successfully!")
    except Exception as e:
        print("Oops! Something goes wrong. {e}")


if __name__ == "__main__":
    main()