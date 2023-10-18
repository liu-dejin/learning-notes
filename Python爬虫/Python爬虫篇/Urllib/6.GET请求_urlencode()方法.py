# urlencode应用场景 多个参数
import urllib.request
import urllib.parse
# https://www.baidu.com/s?wd=周杰伦sex=男
# data ={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location' : '台湾'
# }
# a = urllib.parse.urlencode(data)
# print(a)
# 此时使用urlencode()把整个多参数全部转成unicode码：

# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E5%8F%B0%E6%B9%BE 源码

base_url = 'https://www.baidu.com/s?'
data = {
  'wd' : '周杰伦',
  'sex' : '男',
  'location' : '中国台北'
}

new_data = urllib.parse.urlencode(data)
# 请求地址
url =base_url+new_data

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}
# UA定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟发送请求
response = urllib.request.urlopen(request)
# 获取源码数据
content = response.read().decode('utf-8')
# 打印数据
print(content)