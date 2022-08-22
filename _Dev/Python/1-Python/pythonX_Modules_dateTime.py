
import datetime
import time
import timeit

print(time.ctime())
start_time = time.time()
time.sleep(1)

start_time = timeit.default_timer()

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

now = datetime.datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	