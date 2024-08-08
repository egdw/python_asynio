import asyncio
from aiofiles import open as async_open
import aiohttp


async def async_read_file(file_path: str) -> str:
    async with async_open(file_path, 'r') as f:
        data = await f.read()
        print(data)

    return data


async def async_get_requests(path: str) -> str:
    async  with aiohttp.ClientSession() as session:
        async with session.get(path) as response:
            data = await response.text()
            print(data)
            return data


async def main():
    await asyncio.gather(*[async_read_file('test.txt'), async_get_requests('https://www.baidu.com')])


if __name__ == "__main__":
    asyncio.run(main())
