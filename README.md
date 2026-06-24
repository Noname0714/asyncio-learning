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
```

## 🚀 运行方式
1. 异步爬虫 vs 同步爬虫

```bash
# 运行异步爬虫与同步爬虫对比
python aiohttp+gather.py

```
## 📊 运行结果
性能对比（30个URL）
| 方式 | 耗时	| 说明 |
|------|------|------|
|`同步 (requests)`|	207.11秒 |	逐个请求，总耗时=各请求之和|
|`异步 (aiohttp)`| 2.42秒 |并发请求，总耗时≈最慢那个请求|

结论：异步爬虫速度提升约85.6倍


## 🐛 踩坑记录
坑1：aiohttp连接数限制
现象：并发100个URL时报错 Too many open files

解决：用 asyncio.Semaphore(20) 限制并发数

坑2：Pydantic v1 vs v2 写法不同
现象：from pydantic import BaseModel 报错

解决：检查版本 pip show pydantic，v2用 BaseModel，v1用 BaseModel


## 📝 今日复盘
学会了什么
async/await 本质是协程，不是多线程

asyncio.gather() 可以并发执行多个协程

Semaphore 控制并发数，避免被限流

Pydantic做API数据校验非常方便

明天要改进的
异常处理还不够完善（超时重试）

异步代码调试比同步难，要习惯用 logging

和Agent开发的关系
Agent调用多个工具时可以并发执行，提升响应速度

Pydantic用于解析大模型的JSON输出，确保格式正确

## 📚 参考资料
Python官方asyncio文档

aiohttp官方文档

Pydantic V2文档

B站教程：码农高天

