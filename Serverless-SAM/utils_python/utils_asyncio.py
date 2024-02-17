
# https://www.youtube.com/watch?v=K56nNuBEd0c 

import asyncio
import time

async def brew_coffee():
    print("Start brewCoffee")
    await asyncio.sleep(3)
    print("End brewCoffee")
    return "Coffee ready"

async def toast_bagel():
    print("Start toastBagel")
    await asyncio.sleep(2)
    print("End toastBagel")
    return "Bagel ready"
    

async def main() -> None:

    start = time.perf_counter()

    #batch = asyncio.gather(brew_coffee(), toast_bagel())
    #result_coffee, result_bagel = await batch

    coffee_task = asyncio.create_task(brew_coffee())
    bagel_task = asyncio.create_task(toast_bagel())

    result_coffee = await coffee_task
    result_bagel = await bagel_task

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Time: {time.perf_counter() - start:.2f}")


if __name__ == "__main__":
    asyncio.run(main())