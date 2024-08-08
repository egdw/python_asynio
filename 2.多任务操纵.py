import asyncio


async def print_hello(param: int = 0) -> int:
    print("{}".format(param))
    await asyncio.sleep(2)
    print("{}_1".format(param))
    return param


async def start_task() -> set:
    background_tasks = set()
    # 循环定义task，每个任务启动一个协程
    for p in range(1, 11):
        task = asyncio.create_task(print_hello(param=p))
        background_tasks.add(task)
        # 是否自动移除执行完成后的task任务
        # task.add_done_callback(background_tasks.discard)
    # print(background_tasks)
    # 批量等待
    result = await asyncio.wait(background_tasks)
    for task in background_tasks:
        # 获取每个task中的返回值
        print(task.result())
    # print(result)
    # print(background_tasks)
    return background_tasks


if __name__ == '__main__':

    asyncio.run(start_task())
