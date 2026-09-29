import asyncio


async def hello():
    return "Hello"


async def main():
    result = await hello()
    print(result)


asyncio.run(main())
