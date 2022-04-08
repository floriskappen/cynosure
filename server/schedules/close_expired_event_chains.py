
from apscheduler.schedulers.background import BackgroundScheduler

from entities.event_chains.functions import close_expried

schedulers = []

def schedule():
    # This function may get called twice in development due to the hot reload function. So we keep track of the schedulers to make sure only one is running at a time.
    for scheduler in schedulers:
        scheduler.shutdown()

    scheduler = BackgroundScheduler()
    scheduler.add_job(close_expried, "interval", minutes=1)
    scheduler.start()

    schedulers.append(scheduler)
