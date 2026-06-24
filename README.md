# Day1：Python异步编程 + Pydantic数据校验

> 8周Agent开发学习计划 · 第1天  
> 学习日期：2026-06-22  
> 耗时：上午3h学习 + 下午3h编码 + 晚上2h复盘

---

## 📌 今日目标

- [x] 掌握 `async/await` 语法
- [x] 理解 `asyncio.gather()` 并发执行
- [x] 用 `aiohttp` 实现异步HTTP请求
- [x] 用 `pydantic` 做数据校验和序列化
- [x] 对比同步/异步性能差异

---

## 📂 文件说明

| 文件 | 功能 | 技术点 |
|------|------|--------|
| `hello world.py`|async初步学习尝试|
| `aiohttp-learning.py` | 异步爬虫，并发请求10个URL | asyncio, aiohttp, 信号量控制并发 |
| `aiohttp+gather.py` | 数据校验示例 | BaseModel, Field, validator |
| `requirements.txt` | 依赖清单 | aiohttp, pydantic, requests |

---

## 🔧 环境配置

```bash
# Python版本要求：3.8+
python --version

# 安装依赖
pip install -r requirements.txt
