
import asyncio

def main() -> None:
    try:
        x = 0 / 3
        print("Division: " + x)
    except* (KeyError, ValueError) as e:
       print(e)

async def asyncmain() -> None:
    async with asyncio.TaskGroup as tg:
        task1 = tg.create_task(asyncio.sleep(1))
        print(task1)
        task2 = tg.create_task(asyncio.sleep(2))
        print(task2)
    print("Both tasks have been completed")

    
if __name__ == "__main__":
    main()
    #asyncio.run(asyncmain())