import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 爬虫使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址  第一次访问的地址
    # start_是在allowed_domains前面加一个https://
    # 在其后加上一个/
    start_urls = ["http://www.baidu.com"]

    # 执行start_url之后执行的方法     方法中的response 就是返回的那个对象
    # 相当于 response = urllib.request.urlopen()
    # response = request.get()
    def parse(self, response):
        print('苍茫的天涯是我的爱')
