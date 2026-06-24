import asyncio

async def task(name,dely):
    print(f"{name}开始")
    await asyncio.sleep(dely)
    print(f"{name}结束")
    return f"{name}的结果"

async def main():
    result = await asyncio.gather(
        task("A",2),
        task("B",1),
        task("C",3)
    )
    print(result)

asyncio.run(main())