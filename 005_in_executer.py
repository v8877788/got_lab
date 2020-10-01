"""
    Run slow CPU-intensive or blocking I/O code in a thread:+++

    if a function performs a CPU-intensive calculation for 1 second,
    all concurrent asyncio Tasks and IO operations would be delayed by 1 second.
    An executor can be used to run a task in a different thread or even in a different process
    to avoid blocking block the OS thread with the event loop.
    See the loop.run_in_executor() method for more details.
"""


import asyncio
from urllib.request import urlopen


async def print_data_size():
    data = await get_data_size()
    print("Data size: {}".format(data))


# Note that this is a synchronous function
def sync_get_url(url):
    return urlopen(url).read()


async def get_data_size():
    loop = asyncio.get_event_loop()

    # These each run in their own thread (in parallel)
    future1 = loop.run_in_executor(None, sync_get_url, 'http://xkcd.com')
    future2 = loop.run_in_executor(None, sync_get_url, 'http://google.com')

    # While the synchronous code above is running in other threads, the event loop
    # can go do other things.
    data1 = await future1
    data2 = await future2
    return len(data1) + len(data2)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_data_size())


# sdfgd