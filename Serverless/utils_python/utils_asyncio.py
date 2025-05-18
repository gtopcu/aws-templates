
# https://www.youtube.com/watch?v=K56nNuBEd0c 
# https://www.youtube.com/watch?v=dEZKySL3M9c
# https://www.youtube.com/watch?v=0GVLtTnebNA
# https://www.youtube.com/watch?v=RIVcqT2OGPA
# https://www.youtube.com/watch?v=Qb9s3UiMSTA&t=3s

from typing import Any

import asyncio
from asyncio import TaskGroup, Task, create_task, Future, AbstractEventLoop, TimeoutError, CancelledError

import aiofiles
import aiohttp
import aiosqlite

# !!EventLoop!!
# if __name__ == "__main__":
#     asyncio.run(main())


# async for is used to iterate over an async iterator (objects that implement __aiter__ and __anext__)
# It allows processing items that are retrieved asynchronously
# async def async_generator():
#     # Example async generator that yields numbers with delays
#     for i in range(3):
#         await asyncio.sleep(1)  # Simulating async operation
#         yield i
# async def process_async_items():
#     # Using async for to iterate over async generator
#     async for number in async_generator():
#         print(number)

# async def my_func(delay:float) -> Coroutine[Any, Any, dict[str, str]]:
#     print(f"Waiting for {delay} seconds")
#     await asyncio.sleep(delay)
#     return { "result": f"success - waited for {delay} seconds" }

# async def main():
#     coro = my_func(1) # does not start until awaited or used within a Task
#     result = await coro # await waits for coroutine to finish
#     print(result)

#     task1:Task = create_task(my_func(2))
#     task2:Task = create_task(my_func(4))
#     result1 = await task1 # await does not wait with tasks
#     result2 = await task2 # runs concurrently - like gather()
#     print(result1, result2) # only prints after both tasks are complete

    # await asyncio.sleep(1)
    # asyncio.run(main())
    # await asyncio.Future()  # run forever
    # asyncio.get_running_loop() # get the running event loop, raise exception if there's none
    # task = asyncio.create_task(brew_coffee())
    # asyncio.run(task)
    # task.done()
    # task.cancel()
    # task.cancelled()
    # task.result()

    # asyncio.get_running_loop()
    # asyncio.get_event_loop()
    # await asyncio.gather(task(1), task(2))
    # batch = asyncio.gather(brew_coffee(), toast_bagel())
    # result_coffee, result_bagel = await batch
    # await asyncio.wait([coffee_task, bagel_task])
    # await asyncio.wait_for(coffee_task, timeout=10)

    # coffee_task = asyncio.create_task(brew_coffee())
    # bagel_task = asyncio.create_task(toast_bagel())
    # result_coffee = await coffee_task
    # result_bagel = await bagel_task
    # print(f"Result of brewCoffee: {result_coffee}")
    # print(f"Result of toastBagel: {result_bagel}")
    # print(f"Time: {time.perf_counter() - start:.2f}")

    # await asyncio.gather(*task_list, return_exceptions=True) # runs concurrently
    # results = await asyncio.gather(task1, task2, return_exceptions=True) # runs concurrently
    # for result in results:
    #     print(result)

    # coroutines = [task1(), task2()]
    # await asyncio.gather(*coroutines, return_exceptions=True) # runs concurrently
    # results:Future = await asyncio.gather(task1, task2, return_exceptions=True) # runs concurrently
    # for result in results:
    #     if isinstance(result, Exception):
    #         raise Exception("Error during async processing:" , result)
    #     print(result)

#   coroutines = [task1(), task2()]
#   results = await asyncio.gather(*coroutines, return_exceptions=True)
#     err = None
#     for result, coro in zip(results, coroutines):
#         if isinstance(result, Exception):
#             err = result
#             print(f"{coro.__name__} failed:")
#             traceback.print_exception(type(err), err, err.__traceback__)
#     if err:
#         raise RuntimeError("One or more scripts failed.")


    # TaskGroup - provides error handling. If one task fails, all others are canceled
    # Only moves after the TaskGroup with block after all tasks are finished
    # async with asyncio.TaskGroup() as tg:
    #     task1 = tg.create_task(my_func(1))
    #     task2 = tg.create_task(my_func(2))
    # print("Both tasks have completed now.")

    # tasks = []
    # async with asyncio.TaskGroup() as tg:
    #     for i, sleep_time in enumerate([2, 1, 3], 1):
    #         task = tg.create_task(my_func(sleep_time))
    #         tasks.append(task)
    #         print(f"Scheduled task no {i}")
    
    # results = [task.result() for task in tasks]
    # for result in results:
    #     if isinstance(result, Exception):
    #         raise Exception("Error during async processing:" , result)
    #     print(result)


# Futures
# https://www.youtube.com/watch?v=Qb9s3UiMSTA&t=3s
# async def set_future_result(future, value):
#     await asyncio.sleep(2)
#     # Set the result of the future
#     future.set_result(value)
#     print(f"Set the future's result to: {value}")

# async def main():
#     loop:AbstractEventLoop = asyncio.get_running_loop() # get running event loop, raise exception if there's none
#     future:Future = loop.create_future()

#     # Schedule setting the future's result
#     asyncio.create_task(set_future_result(future, "Future result is ready!"))

#     # Wait for the future's result
#     result = await future
#     print(f"Received the future's result: {result}")


# Synchronization
# shared_resource = 0
# lock = asyncio.Lock()

# async def main():
#     global shared_resource    
#     try:
#         print("Locking..")
#         await lock.acquire()
#         print("Lock acquired")
#         await asyncio.sleep(2)
#     finally:
#         lock.release()
#         print("Lock released")

#     # auto lock.acquire & release
#     async with lock:  
#         print("Lock acquired")
#         await asyncio.sleep(2)
#     print("Lock released")

# Semaphore
# async def access_resource(semaphore, resource_id):
#     async with semaphore:
#         # Simulate accessing a limited resource
#         print(f"Accessing resource with id {resource_id}")
#         await asyncio.sleep(2)
#     print(f"Releasing resource with id {resource_id}")

# async def main():
#     semaphore = asyncio.Semaphore(2) # Allow 2 concurrent access
#     await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

# Event
# async def waiter(event):
#     print("Waiting for the event to be set..")
#     await event.wait() # waits until event.set() is called
#     print("Event has been set, exiting waiter")

# async def setter(event):
#     await asyncio.sleep(2)
#     event.set()
#     print("Event has been set")

# async def main():
#     event = asyncio.Event()
#     await asyncio.gather(waiter(event), setter(event))
    
    
    # server = await asyncio.start_server(lambda: None, "127.0.0.1", 8080)
    # addr = server.sockets[0].getsockname()
    # print(f"Serving on {addr}")

    # async for: This is used to iterate over an async iterator (objects that implement
    # __aiter__ and __anext__). It's particularly useful when you need to process items 
    # that are retrieved asynchronously:

        # async def async_generator():
        #     for i in range(3):
        #         await asyncio.sleep(1)  # Simulating async operation
        #         yield i

        # async def main():
        #     async for number in async_generator():
        #         print(number)
        #         # Do something with each number asynchronously

        # async def read_stream(stream: Iterable) -> None:
        #     async for chunk in stream:
        #         print(chunk)

    # async with: This is used for asynchronous context management (objects that implement 
    # __aenter__ and __aexit__) - used when you need to setup and tear down resources asynchronously:
    
        # async with websockets.serve(self.handle_connection, self.host, self.port):
        #     print(f"WebSocket server started at ws://{self.host}:{self.port}")
        #     await asyncio.Future()

        # async with aiofiles.open("test.txt", "w") as f:
        #     await f.write("Hello, world!")

        # async with aiohttp.ClientSession() as session:
        #     async with session.get("XXXXXXXXXXXXXXXXXXXXXXX") as resp:
        #         print(resp.status)
        #         print(await resp.text())

        # class AsyncResource:
        #     async def __aenter__(self):
        #         print("Acquiring resource")
        #         await asyncio.sleep(1)  # Simulate async setup
        #         return self
        #     async def __aexit__(self, exc_type, exc_val, exc_tb):
        #         print("Releasing resource")
        #         await asyncio.sleep(1)  # Simulate async cleanup

        # async def main():
        #     async with AsyncResource() as resource:
        #         print("Using resource")
        #         await asyncio.sleep(1)
        #
        # # Run with: asyncio.run(main())





    
