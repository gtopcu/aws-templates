
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

print(now)
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(datetime.timezone.utc)


import time
start_time = time.time()
time.sleep(1)
print(time.time() - start_time)