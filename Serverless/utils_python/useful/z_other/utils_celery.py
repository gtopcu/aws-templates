

# https://www.youtube.com/watch?v=THxCy-6EnQM
# pip install celery
# pip install sqlalchemy (if sqlite is used as backend)

# Redis/RabbitMQ as broker + sqlite optional backend
# celery -A tasks worker --loglevel=info

from celery import Celery
# from celery.schedules import crontab
import time

app = Celery('tasks', broker='amqp://guest@localhost//', backend="db+sqlite:///db.sqlite3")

@app.task
def long_running():
    time.sleep(5)
    print("done")

if __name__ == '__main__':
    result = long_running.delay()
    print(result.status)
    print(result.get())
    