import scrapy


class BusSpider(scrapy.Spider):
    name = "bus"
    allowed_domains = ["beijing.8684.cn"]
    start_urls = ["https://beijing.8684.cn/sitemap2"]

    def parse(self, response):
        print("=============")
        name_list = response.xpath('//div//wbfwrap//div[@class="list clearfix"]/a')
        title_list = response.xpath('//div//wbfwrap//div[@class="list clearfix"]/a/@title')

        for i in range(len(name_list)):
            name = name_list[i].extract
            title = title_list[i].extract
            print(name,title)