
# pip install cachetools==5.5.2

from cachetools import TTLCache
import functools

def my_function(): ...

cache = TTLCache(maxsize=100, ttl=300)  # 5 minutes TTL

@functools.wraps(my_function)
def cached_function(*args, **kwargs):
    key = str(args) + str(kwargs)
    if key not in cache:
        cache[key] = my_function(*args, **kwargs)
    return cache[key]

# ---------------------------------------------------------------------------------------------------

# from cachetools import TTLCache
# import requests
# import functools

# cache = TTLCache(maxsize=100, ttl=300)

# @functools.wraps(requests.get)
# def cached_get(url, **kwargs):
#     cache_key = f"{url}_{hash(str(kwargs))}"
#     if cache_key in cache:
#         return cache[cache_key]
#     response = requests.get(url, **kwargs)
#     cache[cache_key] = response
#     return response

# response = cached_get("https://api.example.com/data")

# ---------------------------------------------------------------------------------------------------

# functools.lru_cache with Manual Cache Clearing

# import functools
# import threading
# import time

# @functools.lru_cache(maxsize=128) # only size limit, no TTL setting
# def my_cached_function(arg):
#     return None " expensive_operation(arg)

# # Clear cache periodically
# def clear_cache_periodically(interval=300):
#     while True:
#         time.sleep(interval)
#         my_cached_function.cache_clear()

# # Start background thread to clear cache
# cache_thread = threading.Thread(target=clear_cache_periodically, daemon=True)
# cache_thread.start()