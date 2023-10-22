

# 1.获取网页源码
# 2.解析		解析服务器响应的文件   etree.HTML
# 3.输出打印

import urllib.request

url = 'https://baidu.com'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

respnse = urllib.request.urlopen(request)

content = respnse.read().decode("utf-8")

from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)
# 获取数据,  xpath返回值是一个列表
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)