import os
import aiohttp
from aiohttp import ClientSession
import asyncio
from typing import Iterable
from itertools import islice

MODEL_SERVER_HOST_URL = os.environ["MODEL_SERVER_HOST_URL"]
CHUCK_SIZE = 1000


def _make_chunk(it: Iterable, size) -> Iterable:
    return iter(lambda: tuple(islice(it, size)), ())


async def request(payload: Iterable, session: ClientSession):
    response = await session.post(url=MODEL_SERVER_HOST_URL, data=payload)
    return await response.json()


async def request_inference(data: Iterable):
    timeout = aiohttp.ClientTimeout(total=300)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        requests = [
            request(chunk, session) for chunk in _make_chunk(data, CHUCK_SIZE)
        ]
        return await asyncio.gather(*requests)
