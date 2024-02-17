
####################################################################################################
# 1 - Multiple Except

# def main() -> None:
#     try:
#         x = 0 / 3
#         print("Division: " + x)
#     except* (KeyError, ValueError) as e:
#        print(e)

####################################################################################################
# 2 - asyncio TaskGroups instead of gather

import asyncio

async def asyncfunc(number: int) -> None:
    await asyncio.sleep(number)
    return number

async def main() -> None:
    async with asyncio.TaskGroup as tg:
        task1 = tg.create_task(asyncfunc(1))
        print(task1)
        task2 = tg.create_task(asyncfunc(2))
        print(task2)
    print("Both tasks have been completed")
    
if __name__ == "__main__":
    asyncio.run(main())
    
####################################################################################################