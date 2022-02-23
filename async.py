import time
import asyncio


def http(url):
    time.sleep(3)


async def http2(url):
    print(f'in {url}')
    # http handshake
    time.sleep(1)

    await asyncio.sleep(0)
    print(f'in {url}')

    # batch 1
    await asyncio.sleep(1)
    print(f'in {url}')

    await asyncio.sleep(0)
    print(f'in {url}')

    # batch 2
    await asyncio.sleep(1)
    print(f'in {url}')

    return url


async def delay(msg: str, nr: int):
    c = 0
    for i in range(nr):
        c += 1
        print(f'incremented from {msg}')
        await asyncio.sleep(0)
    print(f'done {msg}')
    return msg


async def main():
    start = time.monotonic()

    one = asyncio.create_task(http2('one'))
    two = asyncio.create_task(http2('two'))

    both = await asyncio.gather(one, two)

    print(f'duration {(time.monotonic() - start):0.2f}')
    print(both)


asyncio.run(main())
