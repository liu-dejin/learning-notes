# post请求
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

data = {
  'kw' : 'spider'
}

# post请求的参数必须编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数是不会拼接到url后面的  而是需要放到定制请求对象的参数中
# post请求的参数必须编码
request = urllib.request.Request(url=url , data=data,headers=headers)

# 模拟发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
# 打印数据
# print(type(content))

# str --> json
import json
obj = json.loads(content)
print(obj)

'''
post请求方式的参数  必须编码  data = urllib.parse.urlencode(data)
编码之后  必须使用encode方法 data = urllib.parse.encode('utf-8')
参数是放在请求对象定制的方法中,request = urllib.request.Request(url=url , data=data,headers=headers)
获取的数据格式是json字符串,我们通过转为json对象能够具体的对获取的数据进行进一步的分析。
'''