import urllib.request

url = 'https://baidu.com'

# url的组成
# https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# http/https  www.baidu.com   80/443
# 协议          主机          端口号
# http 80
# https 443
# mysql 3306
# redis 6379
# mongodb 27017

# response = urllib.request.urlopen(url)
# content = response.read().decode('UTF-8')
# print(content)

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
# urlopen()方法中不能传参字典，因而用户代理UA不能作为传参传入
# 此时需要定制一个请求对象：
# 这里要注意，因为resquest.Resquest()函数有三个传参，这里我们传入两个参数，所以要写成关键字传参
# 如果request = urllib.request.Request(url,headers) 写会报错

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
