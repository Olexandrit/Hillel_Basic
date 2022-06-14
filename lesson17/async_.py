import asyncio


async def sleeper(duration):
    print(f'Sleeping for next {duration} seconds 😴')
    await asyncio.sleep(duration)
    print(f'I slept well for this {duration} seconds')
    
    
async def main():
    await sleeper(1)
    await sleeper(2)
    await sleeper(3)
    
    
asyncio.run(main())


async def main():
    await asyncio.gather(
        sleeper(1),
        sleeper(2),
        sleeper(3),
    )
    
    
asyncio.run(main())


# ---


import asyncio
import random

import httpx  # pip install httpx


async def request_some_important_data(client, number):
    delay = random.randint(1, 10)
    print(f'Requesting very important data #{number} from server')
    await client.get(f'https://httpbin.org/delay/{delay}')
    print(f'Very important data #{number} received')


async def main():
    async with httpx.AsyncClient(timeout=11) as client:
        for i in range(10):
            await request_some_important_data(client, i)


async def main():
    tasks = []
    async with httpx.AsyncClient(timeout=11) as client:
        for i in range(10):
            task = asyncio.create_task(request_some_important_data(client, i))
            tasks.append(task)

        for task in tasks:
            await task


async def main():
    async with httpx.AsyncClient(timeout=11) as client:
        await asyncio.gather(*(request_some_important_data(client, i) for i in range(10)))


if __name__ == '__main__':
    asyncio.run(main())

