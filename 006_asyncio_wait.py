import asyncio


async def foo():
    await asyncio.sleep(1)
    return 42


async def main():
    task = asyncio.create_task(foo())

    print('start...')
    done, pending = await asyncio.wait({task})

    if task in done:
        print('...done')


asyncio.run(main())
