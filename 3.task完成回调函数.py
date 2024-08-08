import asyncio
import requests as rq
from functools import partial


async def get_html(url):
    return rq.get(url).text


# 获取传入参数和运行结果
def html_callback(url, future: asyncio.Future):
    print("url:", url)
    # 获取异步执行返回的结果
    print("future:", future.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html('https://www.baidu.com'))
    # 这里必须使用partial
    task.add_done_callback(partial(html_callback, "https://www.so.com"))
    loop.run_until_complete(task)
    # print(task.result())
