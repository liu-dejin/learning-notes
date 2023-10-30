# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道就必须在setting里面开启管道
class ScrapyDangdangPipeline:
    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 1.write方法必须要写一个字符串  而不能是其他对象
        # 2.w模式会每一个对象都打开一次文件  覆盖之前的内容
        with open('book.json','w',encoding='utf-8')as fp:
            fp.write(str(item))
        return item
