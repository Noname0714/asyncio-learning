import aiohttp   # 导入异步HTTP库
import asyncio   # 导入异步事件循环

async def main():
    # async with → 创建一个会话，用完自动关闭（类似 requests.Session）
    async with aiohttp.ClientSession() as session:
        # session.get() 返回一个响应对象，需要用 async with 进去
        async with session.get("https://httpbin.org/get") as resp:
            # await → 等网络响应回来，再继续
            data = await resp.json()   # 把响应体解析成JSON
            print(data)                # 打印结果

asyncio.run(main())   # 启动
