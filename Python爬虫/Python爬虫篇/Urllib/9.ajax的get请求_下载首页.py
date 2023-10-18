# GET请求
#  获取豆瓣第一页并保存
import urllib.request
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
  'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

# UA定制
request = urllib.request.Request(url=url,headers=headers)
# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')


# 下载到本地
# open方法默认是gbk编码,如果我们保存汉字,那么我们需要在open方法指定一个参数
# encoding='utf-8'
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open ('douban1,json','w',encoding='utf-8') as fp:
  fp.write(content)

# open 方法的返回值赋值给变量 f，当离开 with 代码块的时候，系统会自动调用 f.close() 方法，
# with 的作用和使用 try/finally 语句是一样的