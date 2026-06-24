import requests
import aiohttp
import asyncio
import time
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


# ========== Step 1: 定义 Pydantic 模型 ==========
class HNStory(BaseModel):
    """定义：一个 Hacker News 故事的数据结构"""
    id: int = Field(..., description="故事唯一ID")
    title: str = Field(..., description="标题")
    url: Optional[str] = Field(None, description="故事链接，可能为空")
    score: int = Field(..., description="点赞数")
    by: str = Field(..., description="提交者")
    time: int = Field(..., description="Unix时间戳")
    descendants: Optional[int] = Field(None, description="评论数，可能为空")  # ← 改成可选

    # Pydantic V2 写法：用 model_config 替代 class Config
    model_config = ConfigDict(from_attributes=True)


# ========== Step 2: 同步版爬虫 ==========
def fetch_sync(url: str) -> dict:
    """同步请求一个URL，返回JSON字典"""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


def sync_crawler(story_ids: List[int]) -> List[HNStory]:
    """同步爬虫：逐个请求每个故事详情"""
    stories = []

    for story_id in story_ids:
        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        print(f"[同步] 正在请求故事 {story_id}...")

        data = fetch_sync(url)
        story = HNStory(**data)  # Pydantic 自动验证
        stories.append(story)

    return stories


# ========== Step 3: 异步版爬虫 ==========
async def fetch_async(session: aiohttp.ClientSession, url: str) -> dict:
    """异步请求一个URL，返回JSON字典"""
    async with session.get(url, timeout=10) as resp:
        resp.raise_for_status()
        return await resp.json()


async def async_crawler(story_ids: List[int]) -> List[HNStory]:
    """异步爬虫：并发请求所有故事"""
    async with aiohttp.ClientSession() as session:
        # 创建任务列表（还没执行）
        tasks = [
            fetch_async(session, f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            for sid in story_ids
        ]

        # gather 同时执行所有任务
        raw_results = await asyncio.gather(*tasks, return_exceptions=True)

        # 解析结果
        stories = []
        for data in raw_results:
            if isinstance(data, Exception):
                print(f"⚠️ 请求失败: {data}")
                continue
            story = HNStory(**data)
            stories.append(story)

    return stories


# ========== Step 4: 对比测试 ==========
if __name__ == "__main__":
    # 拿热门故事ID列表
    top_story_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json",
        timeout=10
    ).json()[:30]  # 取前30个

    print(f"📋 共爬取 {len(top_story_ids)} 个故事\n")

    # 同步版
    start = time.time()
    sync_stories = sync_crawler(top_story_ids)
    sync_time = time.time() - start

    # 异步版
    start = time.time()
    async_stories = asyncio.run(async_crawler(top_story_ids))
    async_time = time.time() - start

    # 打印对比
    print(f"{'=' * 50}")
    print(f"🐢 同步版耗时: {sync_time:.2f}秒")
    print(f"⚡ 异步版耗时: {async_time:.2f}秒")
    print(f"🚀 提速: {sync_time / async_time:.1f}x")
    print(f"{'=' * 50}")

    # 打印 TOP 3
    print(f"\n🔥 热门故事 TOP 3:")
    for story in sorted(async_stories, key=lambda s: s.score, reverse=True)[:3]:
        print(f"  #{story.id} {story.title}")
        print(f"     ⭐ {story.score}分 | 💬 {story.descendants or 0}评论 | 👤 {story.by}")
