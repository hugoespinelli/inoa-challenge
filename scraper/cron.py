import schedule
import time
from main import main


print("Initializing scheduler...")
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
