import random
import os

def get_proxy():
    proxy_file = os.path.join('Config', 'proxies.txt')
    if not os.path.exists(proxy_file):
        print(f"Proxy file not found: {proxy_file}")
        return {}

    with open(proxy_file, "r") as file:
        proxies = [line.strip() for line in file if line.strip() and not line.startswith("#")]

    if proxies:
        line = random.choice(proxies).split(":")
        try:
            if len(line) == 2:
                # IP:PORT
                formatted_proxy = ":".join(line)
                proxy = {
                    'http': f'http://{formatted_proxy}',
                    'https': f'https://{formatted_proxy}',
                }
            elif len(line) == 4:
                # IP:PORT:USER:PASS
                formatted_proxy = f'{line[2]}:{line[3]}@{line[0]}:{line[1]}'
                proxy = {
                    'http': f'http://{formatted_proxy}',
                    'https': f'https://{formatted_proxy}'
                }
            else:
                print(f"[ERROR] Failed to parse: {':'.join(line)}")
                proxy = {}
        except Exception as e:
            print(f"[ERROR] Failed to parse: {':'.join(line)}")
            proxy = {}
    else:
        proxy = {}

    return proxy

if __name__ == '__main__':
    print(get_proxy())