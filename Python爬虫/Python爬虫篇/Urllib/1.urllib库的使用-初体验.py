# urllib获取百度首页源码
import urllib.request

# 定义一个url
url = 'http://www.baidu.com'

# 模拟浏览器向浏览器发送请求 response响应
response = urllib.request.urlopen(url)

# 获取响应中的页面的源码 content 内容
# 这里read()函数可以获取响应，但是响应的格式是二进制的，需要解码
# 解码：decode('编码格式')  编码格式在 <head><meta chaset ></head>中显示
content = response.read().decode('utf-8')

print(content)
