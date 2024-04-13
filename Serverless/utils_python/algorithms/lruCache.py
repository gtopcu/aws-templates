
import pprint
from collections import deque, OrderedDict

# Sample LRU cache
class MyCache:

    def __init__(self, capacity: int) -> None:
        self.cache_size = capacity
        self.my_cache = OrderedDict()

    def __str__(self) -> str:
        return self.my_cache.__str__()

    def get_from_cache(self, key: str) -> str:
        if key in self.mycache:
            self.my_cache.move_to_end(key, last=True)
            return self.my_cache[key]
        else:
            return None

    def add_cache(self, key: str, value: str) -> None:
        if self.my_cache.get(key) is None:
            # 1. Check cache size
            # 2. If size <= max, add to cache
            # 3. If size > max, pop first item in cache, add new item to cache
            # 4. Move item to end of cache
            # 5. Return value
            if len(self.my_cache) <= self.cache_size:
                self.my_cache[key] = value
                self.my_cache.move_to_end(key, last=True)
            else:
                self.my_cache.popitem(last=True)
                self.my_cache[key] = value
                self.my_cache.move_to_end(key, last=False)
        else:
            self.my_cache.move_to_end(key, last=True)
        


if __name__ == "__main__":

    cache = MyCache(3)
    cache.add_cache("key-1", "val-1")
    print(cache)
    cache.add_cache("key-2", "val-2")
    print(cache)
    cache.add_cache("key-3", "val-3")
    print(cache)
    cache.add_cache("key-4", "val-4")
    print(cache)



        



        
