import requests

url = 'https://www.baidu.com/s'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}
data = {
	'wd': '北京'
}

# url 请求资源地址
# params 参数
# kwargs 字典
r = requests.get(url=url, params=data, headers=headers)

content = r.text

print(content)

# 总结
# 参数使用params传递参数
# 参数无需urlencode编码
# 不需要请求对象定制
# 请求资源地址的?可加可不加


