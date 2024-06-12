
# https://www.youtube.com/watch?v=FCPBG6NqMmQ

# pip install schedule
import schedule
from schedule import repeat, every, Job
import time
import threading

# @repeat(every(5).seconds, "hello", "world")
def task(arg1, arg2):
    print(arg1, arg2)


schedule.every(2).seconds.until("18:00").do(task, "hello", "world").tag("tag1")
schedule.every(1).hour.at(":30").do(task, "hello", "world")
schedule.every().day.at("16:05:15").do(task, "hello", "world")

job = schedule.every().monday.at("10:30").do(task, "hello", "world")
schedule.cancel_job(job)

jobs: list[Job] = schedule.get_jobs(tag="tag1")
print(jobs)

schedule.run_all(delay_seconds=10)

while True:
    schedule.run_pending()
    time.sleep(1)
    

# Scheduling with threads
#     
# def start_thread(func):
#     thread = threading.Thread(target=func)
#     thread.start()

# def threaded_task():
#     print("threaded task!")

# schedule.every(1).seconds.do(start_thread, threaded_task)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
