from datetime import datetime, timezone
from email_sender import send_email

from scrap import scrap
from load_tables import load_tables
from first_load import first_load
from alert import search_stock_alerts


def send_alerts():
    print("Searching stocks alerts... ")
    alerts = search_stock_alerts()
    print(f"Sending {len(alerts)} alerts...")
    for alert in alerts:
        send_email(**alert)


def main():
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d  %H:%M:%S")
    print(f"Starting scrap and loading tables process at {now} UTC...")
    try:
        scrap()
        first_load()
        load_tables()
        send_alerts()
        print("Scrap and loading tables process ended successfully!")
    except Exception as e:
        print(f"Oops! Something goes wrong. {e}")
