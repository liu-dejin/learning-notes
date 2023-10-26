import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["xa.58.com"]
    start_urls = ["https://xa.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]

    def parse(self, response):
        content = response.text
        print(content)
'''
    字符串   content = response.text
    二进制   content = response.body
    xpath语法 span = response.xpath('//div//table/tbody//a/b')[0]

'''
