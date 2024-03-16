
# https://docs.python.org/3/library/itertools.html

import time
from itertools import batched, count, cycle, repeat, chain, islice

def main() -> None:

    # Infinite operators
    # for val in count(1, 5):
    #     print(val)
    #     time.sleep(1)
    # for val in cycle('ABC'):
    #     print(val)
    #     time.sleep(1)
    # for val in repeat('ABC', 3):
    #     print(val)
    #     time.sleep(1)

    #Iterators
    # for batch in batched('ABCDEFG', 3): #returns tuple
    #     print(batch)
    # for chained in chain('ABC', 'DEF'):
    #     print(chained)
    # for chained in chain.from_iterable(chain.from_iterable(['ABC', 'DEF'])): 
    #     print(chained)
    # for islice_val in islice('ABCDEFG', 2, None, 1):
    #     print(islice_val)


if __name__ == "__main__":
    main()
