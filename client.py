import asyncio
import grpc
import json
import time
import sys

import users_pb2
import users_pb2_grpc
from aiohttp import ClientSession

REQUESTS = 20000


def log(method):
    async def logged(*args, **kw):
        print(f'\n+-------------- {method.__name__.upper()} ---------------\n+')
        start = time.time()
        size = await method(*args, **kw)

        duration = time.time() - start
        print('+  total time [seconds]  : ' + str(round(duration, 5)))
        print('+  total size [MB]       : ' + str(round(size / 1024 / 1024, 2)))
        print('+  ops/second            : ' + str(round(REQUESTS / duration)))
        print('+  avg. response time    : ' + str(round(duration / REQUESTS, 8)))
        print(f'+\n+---------------------------------------\n')

    return logged


@log
async def run_grpc():
    channel = grpc.insecure_channel('[::]:50051')
    stub = users_pb2_grpc.UsersStub(channel)

    request = users_pb2.UsersRequest()
    size = 0
    for _ in range(REQUESTS):
        response = stub.get(request)
        size += response.ByteSize()

    return size


@log
async def grpc_stream():
    channel = grpc.insecure_channel('[::]:50051')
    stub = users_pb2_grpc.UsersStub(channel)

    request = users_pb2.UsersRequest()
    responses = stub.get_stream(request)

    size = 0
    for response in responses:
        size += response.ByteSize()

    return size


@log
async def run_rest():
    size = 0

    async with ClientSession() as session:
        for _ in range(REQUESTS):
            async with session.get('http://localhost:8000/users') as response:
                text = await response.text()
                size += sys.getsizeof(text)
                json.loads(text)

    return size


loop = asyncio.get_event_loop()
loop.run_until_complete(run_rest())
loop.run_until_complete(run_grpc())
loop.run_until_complete(grpc_stream())
