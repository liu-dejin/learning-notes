# 1,请求对象的定制
# 2.获取网页掩码
# 3.下载


import urllib.request
from lxml import etree


def create_request():
	url = 'https://sc.chinaz.com/tupian/gudianmeinvtupian.html'

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}

	request = urllib.request.Request(url=url,headers=headers)

	return request



def get_content(request):
	response = urllib.request.urlopen(request)
	content = response.read().decode("utf-8")
	return content


def down_load(content):
	# urllib.request.urlretrieve('图片地址','文件的名字')
	tree = etree.HTML(content)

	name_list = tree.xpath('/html/body//div//img/@alt')
	# 一般设计到图片的网站都会懒加载	src2-->src
	src_list = tree.xpath('/html/body//div//img/@data-original')

	# print(name_list,src_list)

	for i in range(len(src_list)):
		src = src_list[i]
		name = name_list[i]
		urllib.request.urlretrieve(url=src,filename= './img' + name + '.jpg')


if __name__ == '__main__':
	# 请求对象定制
	request = create_request()
	# 获取网页源码
	content = get_content(request)
	# 下载
	down_load(content)




