# URLerror.HTTPError
# thhperror 是url的子类

import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/qq_52736131/article/details/123251131'
url = 'http://goudan111.com'


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

try:
	request = urllib.request.Request(headers=headers, url=url)

	response = urllib.request.urlopen(request)

	content = response.read().decode('utf-8')

	print(content)
except urllib.error.HTTPError:
	print("系统正在升级")
except urllib.error.URLError:
	print("你错了")