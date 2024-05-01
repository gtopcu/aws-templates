
# https://github.com/geeogi/async-python-lambda-template

import asyncio
import aiobotocore
import aiohttp

# # The AWS Lambda handler
# def handler(event, context):
#     asyncio.run(main())

# async def main():
#     # Here you can await any awaitable
#     await asyncio.sleep(1)
#     await asyncio.gather([coroutine_1, coroutine_2])


# import asyncio
# import traceback

# import aiobotocore
# import aiohttp

# from scripts.bitcoin_news import bitcoin_news
# from scripts.bitcoin_price import bitcoin_price

# async def main():
#     async with aiobotocore.get_session().create_client('s3', region_name='eu-west-2') as s3_client:
#         async with aiohttp.ClientSession() as session:
#             coroutines = [
#                 bitcoin_price(session, s3_client),
#                 bitcoin_news(session, s3_client),
#             ]
#             results = await asyncio.gather(*coroutines, return_exceptions=True)

#     err = None
#     for result, coro in zip(results, coroutines):
#         if isinstance(result, Exception):
#             err = result
#             print(f"{coro.__name__} failed:")
#             traceback.print_exception(type(err), err, err.__traceback__)

#     if err:
#         raise RuntimeError("One or more scripts failed.")


# def handler(event, context):
#     asyncio.run(main())