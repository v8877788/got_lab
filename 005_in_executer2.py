"""
    The executor argument should be an concurrent.futures.Executor instance.
    The default executor is used if executor is None
"""

import asyncio
import concurrent.futures


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 8))


async def main():
    loop = asyncio.get_running_loop()

    #
    # The executor argument should be an concurrent.futures.Executor instance.
    # The default executor is used if executor is None
    #

    # Options:
    if 0 and "1. Run in the default loop's executor":
        result = await loop.run_in_executor(
            None,
            blocking_io
        )
        print('default thread pool', result)

    if 1 and '2. Run in a custom thread pool':
        with concurrent.futures.ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool,
                blocking_io
            )
            print('custom thread pool', result)

    if 0 and '3. Run in a custom process pool':
        with concurrent.futures.ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool,
                cpu_bound
            )
            print('custom process pool', result)


asyncio.run(main())