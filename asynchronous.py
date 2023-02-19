import asyncio
import aiohttp

async def check_proxy(proxy, session):
    proxy = proxy.strip()
    try:
        for protocol in ['http', 'https', 'socks4', 'socks5']:
            proxy_dict = {protocol: f"{protocol}://{proxy}"}
            async with session.get("https://www.google.com", proxy=proxy_dict, timeout=5) as response:
                if response.status == 200:
                    with open('working_proxies.txt', 'a') as f:
                        f.write(f"{protocol}://{proxy}\n")
                        print(f"{protocol}://{proxy} working")
    except:
        print(f"{proxy} not working")

async def check_proxies(file_path):
    async with aiohttp.ClientSession() as session:
        with open(file_path, "r") as f:
            proxies = f.readlines()

        tasks = []
        for proxy in proxies:
            task = asyncio.create_task(check_proxy(proxy, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

file_path = input("Введите путь к файлу с прокси: ")
asyncio.run(check_proxies(file_path))
