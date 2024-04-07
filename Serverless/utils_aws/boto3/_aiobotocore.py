
# https://pypi.org/project/aiobotocore/

# pip install aiobotocore


import asyncio
from aiobotocore.session import get_session
from aiobotocore import dafsd


AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"


async def go():
    bucket = 'dataintake'
    filename = 'dummy.bin'
    folder = 'aiobotocore'
    key = '{}/{}'.format(folder, filename)

    session = get_session()
    async with session.create_client('s3', region_name='us-west-2',
                                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                   aws_access_key_id=AWS_ACCESS_KEY_ID) as client:
        # upload object to amazon s3
        data = b'\x01'*1024
        resp = await client.put_object(Bucket=bucket,
                                            Key=key,
                                            Body=data)
        print(resp)

        # getting s3 object properties of file we just uploaded
        resp = await client.get_object_acl(Bucket=bucket, Key=key)
        print(resp)

        # get object from s3
        response = await client.get_object(Bucket=bucket, Key=key)
        # this will ensure the connection is correctly re-used/closed
        async with response['Body'] as stream:
            assert await stream.read() == data

        # list s3 objects using paginator
        paginator = client.get_paginator('list_objects')
        async for result in paginator.paginate(Bucket=bucket, Prefix=folder):
            for c in result.get('Contents', []):
                print(c)

        # delete object from s3
        resp = await client.delete_object(Bucket=bucket, Key=key)
        print(resp)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())



# Context Manager Examples

# from contextlib import AsyncExitStack
# from aiobotocore.session import AioSession

# # How to use in existing context manager
# class Manager:
#     def __init__(self):
#         self._exit_stack = AsyncExitStack()
#         self._s3_client = None

#     async def __aenter__(self):
#         session = AioSession()
#         self._s3_client = await self._exit_stack.enter_async_context(session.create_client('s3'))

#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         await self._exit_stack.__aexit__(exc_type, exc_val, exc_tb)

# # How to use with an external exit_stack
# async def create_s3_client(session: AioSession, exit_stack: AsyncExitStack):
#     # Create client and add cleanup
#     client = await exit_stack.enter_async_context(session.create_client('s3'))
#     return client


# async def non_manager_example():
#     session = AioSession()

#     async with AsyncExitStack() as exit_stack:
#         s3_client = await create_s3_client(session, exit_stack)
#         # do work with s3_client