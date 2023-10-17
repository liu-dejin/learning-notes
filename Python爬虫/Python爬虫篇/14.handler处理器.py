import urllib.request

# 首先通过urllib库新建一个handler对象，
# 而后通过urllib库的build_opener()方法新建一个opener对象，其中build_opener()要传入handler对象，
# 最后通过opener的open()方法，获取响应，传参是我们的request定制请求对象

url = 'http://baidu.com'

headrers =  {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headrers)
# handler build_opener open

# 1.获取handler对象
handler = urllib.request.HTTPHandler()

# 2.opener对象获取

opener = urllib.request.build_opener(handler)

# 3调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)