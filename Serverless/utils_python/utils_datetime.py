
from datetime import datetime, timedelta, timezone, UTC
# import datetime
# from pytz import timezone
# import isodate

# datetime.now(timezone.utc)
# datetime.now(timezone.utc).isoformat(timespec="seconds") # 2025-01-12T18:03:54+00:00 
# datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# datetime.utcnow()
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# date.today()
# date.day
# date.month
# date.year
# date = datetime.strptime("2024-03-24", "%Y-%m-%d").date()
# birthday = datetime.strptime("2020-07-24", "%Y-%m-%d").date()
# age = (date.today() - birthday).days // 365
# print(age)

DATE_FORMAT : str           = "%Y-%m-%d %H:%M:%S"   # 2024-03-24 14:03:42
DATE_FORMAT_ISO : str       = "%Y-%m-%dT%H:%M:%S"   # 2024-03-24T14:03:42 #ISO8601 
DATE_FORMAT_ISO_TZ: str     = "%Y-%m-%dT%H:%M:%S%Z" # 2024-03-24T14:03:42+03

# print(datetime.now())
# date_time = datetime(2024, 11, 8, 12, 15, 00, tzinfo=UTC)
# print(datetime.now().isoformat())
# print(datetime.strftime(datetime.now(), DATE_FORMAT_ISO_TZ))
    
# datetime(2020, 5, 17, tzinfo=UTC) # hour, minute, second, microsecond, tzone=None
# datetime.now().replace(days=0, minutes=0, seconds=0, microsecond=0)
# datetime.now() + timedelta(days=1, hours=2)
# print(datetime.now() > date)

# date = datetime.fromisoformat("2024-02-20T13:55:05")
# datetime.fromisocalendar(2020, 5, 17)
# datetime.fromtimestamp(time.time())

# now = datetime.now() # tz=UTC
# print(now)                                            # 2024-03-20 12:57:32.133498
# datetime.utcnow()
# print(now.isoformat())                                # 2024-03-20T12:57:32.133498 -> ISO8601 - since Python3.6
# print(now.astimezone())                               # 2024-03-20 12:58:36.424456+03:00
# print(now.strftime("%Y-%m-%d %H:%M:%S"))              # 2024-03-20T12:59:21
# print(now.strftime("%A %B %d-%m-%Y %I:%M:%S%p %z"))   # Wednesday March 20-03-2024 01:19:52PM +0300
# print(now.strftime("%A %x %X"))                       # Wednesday 03/20/24 13:04:36
# print(f"{now:%Y-%m-%dT%H:%M:%SZ}")                    # 2024-03-20T12:59:21Z
# print(f"{now:%c}")                                    # Wed Mar 20 13:03:06 2024 -> local

# utc = timezone("UTC")
# loc = utc.localize(datetime.now())
# print(loc)                                      # 2024-03-20 13:29:21.535102+00:00
# local_tz = timezone("Europe/Istanbul")          # Europe/Amsterdam, Australia/Sydney, Asia/Tokyo, US/Eastern
# print(loc.astimezone(local_tz))                 # 2024-03-21 00:34:03.881096+11:00

# ---------------------------------------------------------------------------------------------------

# import time
# import timeit

# time.sleep(1)
# print(time.time()) 
# epoch = time.mktime((2024, 3, 24, 0, 0, 0, 0, 0, -1))
# print(time.localtime())
# print(time.gmtime())
# print(time.asctime((2024, 3, 24, 0, 0, 0, 0, 0, -1)))
# print(time.strftime("%Y-%m-%d %H:%M:%S%z")) #, time.localtime(epoch))
# print(time.strptime("2024-03-24", "%Y-%m-%d"))
# time.perf_counter()
# time.time_ns()
# time.monotonic()
# time.process_time() 
# time.thread_time()
# timeit.timeit("x = 1", number=1000)
# timeit.repeat("x = 1", repeat=3, number=1000)
# timeit.Timer("x = 1").timeit(number=1000)
# timeit.Timer("x = 1").repeat(repeat=3, number=1000)
# timeit.Timer("x = 1").autorange()

# ------------------------------------------------------------------------------------------------------------------------

# import pendulum

# now = pendulum.now()
# print(now)

# now = now.in_timezone("Asia/Tokyo")
# print(now)
# print(now.to_iso8601_string())

# now = now.add(years=1).add(days=3).add(hours=2)
# print(now)


