# from datetime import datetime, timedelta, UTC
import datetime
import time
# from pytz import timezone
# import isodate

DATE_FORMAT : str           = "%Y-%m-%d %H:%M:%S"   # 2024-03-24 14:03:42
DATE_FORMAT_ISO : str       = "%Y-%m-%dT%H:%M:%S"   # 2024-03-24T14:03:42 #ISO8601 
DATE_FORMAT_ISO_TZ: str     = "%Y-%m-%dT%H:%M:%S%Z" # 2024-03-24T14:03:42+03

def get_time() -> str:
    return time.strftime(DATE_FORMAT)

def get_time_iso() -> str:
    return time.strftime(DATE_FORMAT_ISO)

def get_time_iso_tz() -> str:
    return time.strftime(DATE_FORMAT_ISO_TZ)

# datetime.datetime(2020, 5, 17, tzinfo=UTC) # hour, minute, second, microsecond, tzone=None
# datetime.datetime.now().replace(days=0, minutes=0, seconds=0, microsecond=0)
# datetime.datetime.now() + datetime.timedelta(days=1, hours=2)
# print(datetime.now() > date)
# datetime.utcnow())

# date = datetime.fromisoformat("2024-02-20T13:55:05")
# datetime.fromisocalendar(2020, 5, 17)
# datetime.fromtimestamp(time.time())

# now: datetime = datetime.now() # tz=UTC
# print(now)                                            # 2024-03-20 12:57:32.133498
# print(now.isoformat())                                # 2024-03-20T12:57:32.133498 -> ISO8601 - since Python3.6
# print(now.astimezone())                               # 2024-03-20 12:58:36.424456+03:00
# print(now.strftime("%Y-%m-%d %H:%M:%S"))              # 2024-03-20T12:59:21
# print(now.strftime("%A %B %d-%m-%Y %I:%M:%S%p %z"))   # Wednesday March 20-03-2024 01:19:52PM +0300
# print(now.strftime("%A %x %X"))                       # Wednesday 03/20/24 13:04:36
# print(f"{now:%Y-%m-%dT%H:%M:%SZ}")                    # 2024-03-20T12:59:21Z
# print(f"{now:%c}")                                    # Wed Mar 20 13:03:06 2024 -> local

# print(time.time())                                    # 1710929397.2372649
# print(time.time_ns())                                 # 1710929428977893000
# print(time.gmtime())

# utc = timezone("UTC")
# loc = utc.localize(datetime.now())
# print(loc)                                      # 2024-03-20 13:29:21.535102+00:00
# local_tz = timezone("Europe/Istanbul")          # Europe/Amsterdam, Australia/Sydney, Asia/Tokyo, US/Eastern
# print(loc.astimezone(local_tz))                 # 2024-03-21 00:34:03.881096+11:00


# ------------------------------------------------------------------------------------------------------------------------

# import pendulum

# now = pendulum.now()
# print(now)

# now = now.in_timezone("Asia/Tokyo")
# print(now)
# print(now.to_iso8601_string())

# now = now.add(years=1).add(days=3).add(hours=2)
# print(now)



