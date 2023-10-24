import requests
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

data = {
	'kw':'eye'
}

# url请求地址
# data请求参数
# kwargs  字典
r = requests.post(url=url , data=data,headers=headers)

content = r.text

import json

obj = json.loads(content)

print(obj)

# 总结
# post请求不需要编解码
# 请求参数是data
# 不需要请求对象的定制


