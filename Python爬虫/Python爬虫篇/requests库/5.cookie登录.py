# 通过登录进入到主页面

# 登录接口参数很多

# __VIEWSTATE: y+4GFdgtoitoCFwPgQbR+rpOAQF8QY+0FgaE6wIP3qCGatEFLdFYSS3lTNA5UvF3s1dPZmxv9W+qQgAH1MT/EoDhPuxKos7ck92kFOQewC2M3ZDxNL3FfXOWf/ZE8NPBSI6yToSgNisXqMTijWrIJxGhYvc=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 15929539511
# pwd: l20021111
# code: NHHI
# denglu: 登录

# __VIEWSTATE	__VIEWSTATEGENERATOR	code是一个变化的值

# 难点  (1)__VIEWSTATE	__VIEWSTATEGENERATOR	一般情况下看不到的数据在页面源码中
# 解析页面源码
# (2)验证码

import requests

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

r = requests.get(url=url, headers=headers)

content = r.text
# 获取 __VIEWSTATE	__VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取 __VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = "https://so.gushiwen.cn" + code


# 有坑
# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# requests有一个方法session	请求变成一个对象

session = requests.session()
# 验证码的url的内容
r_code = session.get(code_url)
# 此时注意我们要使用二进制数据.因为我们使用的是图片的下载
content_code = r_code.content
# wb就是将二进制数据写入文件
with open('code.jpg','wb') as fp:
	fp.write(content_code)


# 获取了验证码的图片下载到本地,观察之后在控制台输入验证码就可以得到code参数
code_name = input("请输入你的验证码")

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
	'__VIEWSTATE': viewstate,
	'__VIEWSTATEGENERATOR': viewstategenerator,
	'from: http': '//so.gushiwen.cn/user/collect.aspx',
	'email': ' 1593339539533311',
	'pwd': ' l2002t671110',
	'code': code_name,
	'denglu': ' 登录',
}
r_post = session.post(url=url,headers=headers,data=data_post)
content_post = r_post.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
	fp.write(content_post)


# 难点
# 验证码
# 隐藏域
