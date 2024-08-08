import asyncio
import random


async def hello() -> int:
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    return random.randint(1, 10)


async def main():
    # gather 可以合并两个任务同时执行
    result = await asyncio.gather(hello(), hello())
    # [3,7] 最后会以数组的形式返回
    print(result)
    print("aa")


# task写法测试
async def task_test():
    task = asyncio.create_task(hello())
    task.cancel()
    # 取消后的任务不可以继续进行
    await task


if __name__ == "__main__":
    # 还有一种写法，和这种是一致的。
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello())
    # loop.close()
    asyncio.run(task_test())
