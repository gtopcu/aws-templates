
# https://www.youtube.com/watch?v=K56nNuBEd0c 

import asyncio
import time

def brewCoffee():
    print("Start brewCoffee")
    time.sleep(3)
    print("End brewCoffee")
    return "Coffee ready"

def toastBagel():
    print("Start toastBagel")
    time.sleep(2)
    print("End toastBagel")
    return "Bagel ready"
    

def main() -> None:

    start = time.perf_counter

    brewCoffee()
    toastBagel()

    print(f"Time: {time.perf_counter() - start:.2f}")


if __name__ == "__main__":
    main()