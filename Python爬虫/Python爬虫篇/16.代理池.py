# 代理池的使用
import urllib.request
import random

proxies_pool = [
	{'http': '27.203.215.138:8060'},
	{'http': '40.83.102.86:80'},
	{'http': '14.215.212.37:9168'}
]

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('dail2.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
