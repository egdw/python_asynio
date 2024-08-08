import requests as rq
import asyncio


async def get_html(path="") -> str:
    return rq.get(path).text


async def main():
    result = await asyncio.gather(*[get_html("https://www.baidu.com"),
                                    get_html("https://www.so.com"), ])
    print(result)


if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
