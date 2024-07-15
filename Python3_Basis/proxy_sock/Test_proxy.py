
import requests
def test_proxy(proxy_url, username, password, test_url):
    proxies = {
        'http': f'socks5h://{username}:{password}@{proxy_url}',
        'https': f'socks5h://{username}:{password}@{proxy_url}',
    }
    print(proxies)
    try:
        response = requests.get(test_url, proxies=proxies, verify=False)
        print(f"Proxy {proxy_url} is working. Status code: {response.status_code}")
        print(f"Response length: {len(response.text)}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy_url} failed. Error: {e}")




if __name__ == "__main__":
    # 代理服务器地址和端口，例如 '127.0.0.1:8080'
    proxy_url = '127.0.0.1:8080'
    # 代理服务器的用户名和密码
    username = 'root'
    password = 'root'
    # 测试的 URL，例如 'http://www.google.com'
    test_url = 'http://www.google.com'
    test_proxy(proxy_url, username, password, test_url)