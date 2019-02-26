import schedule
import time

def job():
    """Show that scheduling is working, and also how to write a docstring."""

    print("I'm working continuously...")


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)


# Uncomment the below for a job that runs every ten minutes.
"""
schedule.every(10).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
"""

print("I'm working.")