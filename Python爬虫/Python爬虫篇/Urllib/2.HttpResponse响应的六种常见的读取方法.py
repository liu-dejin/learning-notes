import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器发出请求
response = urllib.request.urlopen(url)

# HTTPResponse这个类型
# 六个方法：read、readline、readlines、getcode、geturl、getheaders
# response = urllib.request.urlopen(url)
# print(type(response)) # response是HTTPResponse的类型

print(type(response)) #<class 'http.client.HTTPResponse'>

# 按照一个字节一个字节去读
content = response.read()
print(content)
# 读取具体的n个字节，在read()函数中传参即可
content2 = response.read(5)
print(content2)

# 读取一行
content3 = response.readline()
print(content3)

# 按行读取，并且读取所有行
content4 = response.readlines()
print(content4)

# 返回状态码  200状态码没有问题，其他的状态码可能有问题
print(response.getcode())

# 返回url地址
print(response.geturl())

# 获取响应头
print(response.getheaders())


