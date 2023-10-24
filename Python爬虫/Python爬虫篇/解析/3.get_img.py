# 1,请求对象的定制
# 2.获取网页掩码
# 3.下载


import urllib.request
from lxml import etree
from io import BytesIO
import gzip


def create_request():
    url = 'https://sc.chinaz.com/tupian/meishitupian.html'

    headers = {
        'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.9',
        'Cache-Control': ' no-cache',
        'Connection': ' keep-alive',
        'Cookie': ' cz_statistics_visitor=c0ef209e-abc5-8487-64ef-8fe1879db9b4; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1697644485,1697686571; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1697686571',
        'Host': ' sc.chinaz.com',
        'Pragma': ' no-cache',
        'Sec-Fetch-Dest': ' document',
        'Sec-Fetch-Mode': ' navigate',
        'Sec-Fetch-Site': ' none',
        'Sec-Fetch-User': ' ?1',
        'Upgrade-Insecure-Requests': ' 1',
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'sec-ch-ua': ' "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': ' ?0',
        'sec-ch-ua-platform': ' "Windows"',
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    # read()方法查看爬取内容时发现它是以"b’\x1f\x8b\x08"开头 ，它是gzip压缩数据
    buff_response = BytesIO(response.read())
    f = gzip.GzipFile(fileobj=buff_response)
    return f.read().decode('utf-8')


def down_load(content):
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)

    name_list = tree.xpath('//html/body//div//img/@alt')
    # 一般设计到图片的网站都会懒加载	src2-->src
    src_list = tree.xpath('//html/body//div//img/@data-original')

    # 打印测试
    # print(name_list,src_list)

    for i in range(len(src_list)):
        src = "https:" + src_list[i]
        name = name_list[i]
        urllib.request.urlretrieve(url=src, filename= './img/' + name + '.jpg')


if __name__ == '__main__':
    # 请求对象定制
    request = create_request()
    # 获取网页源码
    content = get_content(request)
    # 下载
    down_load(content)
