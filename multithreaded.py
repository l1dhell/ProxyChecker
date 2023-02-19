import requests
import concurrent.futures

def check_proxy(proxy):
    proxy = proxy.strip()
    try:
        for protocol in ['http', 'https', 'socks4', 'socks5']:
            proxy_dict = {protocol: f"{protocol}://{proxy}"}
            response = requests.get("https://www.google.com", proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                with open('working_proxies.txt', 'a') as f:
                    f.write(f"{protocol}://{proxy}\n")
                    print(f"{protocol}://{proxy} is working")
    except:
        print(f"{proxy} is not working")

def check_proxies(file_path, num_threads=10):
    with open(file_path, "r") as f:
        proxies = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(check_proxy, proxies)

file_path = input("Введите путь к файлу с прокси: ")
num_threads = int(input("Введите количество потоков: "))
check_proxies(file_path, num_threads)
