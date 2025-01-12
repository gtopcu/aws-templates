
# https://www.youtube.com/watch?v=K56nNuBEd0c 
# https://www.youtube.com/watch?v=dEZKySL3M9c
# https://www.youtube.com/watch?v=0GVLtTnebNA
# https://www.youtube.com/watch?v=RIVcqT2OGPA

import asyncio
import aiofiles
import aiohttp
import aiosqlite
import time

async def main() -> None:

    start = time.perf_counter()

    # asyncio.run(main())
    # await asyncio.Future()  # run forever
    # await asyncio.gather(*task_list, return_exceptions=True)
    # await asyncio.sleep(1)
    # task = asyncio.create_task(brew_coffee())
    # asyncio.run(task)
    # task.done()
    # task.cancel()
    # task.cancelled()
    # task.result()
    # asyncio.TimeoutError, asyncio.CancelledError

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

#   async with asyncio.TaskGroup as tg:
#       task1 = tg.create_task(asyncfunc(1))
#       print(task1)
#       task2 = tg.create_task(asyncfunc(2))
#       print(task2)
#   print("Both tasks have been completed")

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






if __name__ == "__main__":
    asyncio.run(main())


    
