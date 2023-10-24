import requests

url = 'https://www.baidu.com/s?'



headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

data = {
	'wd' : 'ip'
}

proxy = {
	'http' : '117.24.81.194:8888'
}


r = requests.get(url=url,params=data,headers=headers,proxies=proxy)

content = r.text

with open('daili.html','w',encoding='utf-8')as fp:
	fp.write(content)