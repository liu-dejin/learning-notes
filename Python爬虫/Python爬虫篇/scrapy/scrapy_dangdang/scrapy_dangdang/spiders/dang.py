import scrapy

from scrapy_dangdang.items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.06.06.00.00.html"]

    def parse(self, response):
        # pipeline 下载数据
        # items  定义数据结构    你要下载的数据都有什么

#         所有的seletor的对象都可以调用xpath方法

        li_list = response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他的属性不一样    第一张的scr是可以用的  其他的是data-original
            if src :
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            print(src,name)

            book = ScrapyDangdangItem(scr = src , name = name )

#           获取一个book就就将book交给pipeline
            yield book

# 每一页业务逻辑是一样的，所以后续页面直接调用即可