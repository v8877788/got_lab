import asyncio


async def print_every_second():
    """Print seconds"""
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


async def print_every_5second():
    for i in range(2):
        await asyncio.sleep(5)
        print(i, '5second')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_every_second(),
                   print_every_5second())
)
loop.close()
