import urllib.request
import urllib.parse


def get_page_url(start_page, end_page):
	url = 'https://beijing.8684.cn/list'
	url_dict = {}
	for page in range(start_page, end_page + 1):
		url_dict[page] = url + str(page)
	return url_dict
url_dict = get_page_url(1,9)
print(url_dict)