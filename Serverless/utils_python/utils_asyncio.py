
# https://www.youtube.com/watch?v=K56nNuBEd0c 
# https://www.youtube.com/watch?v=dEZKySL3M9c
# https://www.youtube.com/watch?v=0GVLtTnebNA

import asyncio
import time
from collections.abc import Iterable

async def brew_coffee():
    yield b"yielding"
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

    # asyncio.get_running_loop()
    # asyncio.get_event_loop()
    # asyncio.run(brew_coffee())
    # await asyncio.gather(task(1), task(2))
    # await asyncio.gather(*task_list, return_exceptions=True)
    # await asyncio.sleep(1)
    # task = asyncio.create_task(task(3))
    # await asyncio.wait([coffee_task, bagel_task])
    # await asyncio.wait_for(coffee_task, timeout=10)
    # task.done()
    # task.cancel()
    # task.cancelled()
    # result task.result()
    # asyncio.TimeoutError, asyncio.CancelledError

    coffee_task = asyncio.create_task(brew_coffee())
    bagel_task = asyncio.create_task(toast_bagel())

    result_coffee = await coffee_task
    result_bagel = await bagel_task

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Time: {time.perf_counter() - start:.2f}")

#   coroutines = [ task1(), task2() ]
#   results = await asyncio.gather(*coroutines, return_exceptions=True)
#     err = None
#     for result, coro in zip(results, coroutines):
#         if isinstance(result, Exception):
#             err = result
#             print(f"{coro.__name__} failed:")
#             traceback.print_exception(type(err), err, err.__traceback__)
#     if err:
#         raise RuntimeError("One or more scripts failed.")

async def read_stream(stream: Iterable) -> None:
    async for chunk in stream:
        print(chunk)

async def generator_func(loop_count: int):
    for i in range(loop_count):
        yield i
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())


# https://www.youtube.com/watch?v=dEZKySL3M9c
# async def main():
#     async for chunk in stream:
#         pass   



####################################################################################################
# asyncio TaskGroups instead of gather

# import asyncio

# async def asyncfunc(number: int) -> None:
#     await asyncio.sleep(number)
#     return number

# async def main() -> None:
#     async with asyncio.TaskGroup as tg:
#         task1 = tg.create_task(asyncfunc(1))
#         print(task1)
#         task2 = tg.create_task(asyncfunc(2))
#         print(task2)
#     print("Both tasks have been completed")
    
# if __name__ == "__main__":
#     asyncio.run(main())

####################################################################################################