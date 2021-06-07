from datetime import datetime, timezone
from email_sender import send_email

from scrap import scrap
from load_tables import load_tables
from first_load import first_load


def search_for_alerts():
    return [
        {
            "stock": "PETR4",
            "action": "Venda",
            "price": 1992,
            "user_email": "example@gmail.com",
        }
    ]


def main():
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d  %H:%M:%S")
    print(f"Starting scrap and loading tables process at {now} UTC...")
    try:
        # scrap()
        # first_load()
        # load_tables()
        alerts = search_for_alerts()
        for alert in alerts:
            send_email(**alert)
        print("Scrap and loading tables process ended successfully!")
    except Exception as e:
        print(f"Oops! Something goes wrong. {e}")


if __name__ == "__main__":
    main()