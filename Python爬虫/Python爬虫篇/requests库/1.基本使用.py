import requests

url = 'http://www.baidu.com'

r = requests.get(url=url)

'''
r.text : 获取网站源码
r.encoding ：访问或定制编码方式
r.url ：获取请求的url
r.content ：响应的字节类型
r.status_code ：响应的状态码
r.headers ：响应的头信息
'''

# 一个类型和六个属性
print(type(r))	#Response类型

# 设置响应的编码格式
r.encoding='utf-8'

# 以字符串形式返回了网页的源码
print(r.text)

# 返回url的路径
print(r.url)

# 返回的是二进制地址
print(r.content)

# 返回响应的状态码
print(r.status_code)

# 返回响应头
print(r.headers)

