# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 获取https://www.baidu.com/s?wd=周杰伦 的网页源码
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='

# UA定制  解决反爬的第一种方案
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}
# 将周杰伦三个字变成unicode编码形式
# 依赖于urilib.parse
name = urllib.parse.quote('周杰伦')

url = url + name



#  UA定制
request = urllib.request.Request(url=url,headers=headers)


# 模拟发送请求
response = urllib.request.urlopen(request)

# 获取请求后的内容
content = response.read().decode('utf-8')

# 打印数据
print(content)