import asyncio

async def hello():
    print("你好")
    await asyncio.sleep(1)
    print("世界")

asyncio.run(hello())