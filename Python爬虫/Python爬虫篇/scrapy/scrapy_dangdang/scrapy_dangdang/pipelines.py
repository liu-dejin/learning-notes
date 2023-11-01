# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

import urllib3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道就必须在setting里面开启管道
class ScrapyDangdangPipeline:
	# 爬虫开始执行
	def open_spider(self, spider):
		self.fp = open('book.json', 'w', encoding='utf-8')

	# item就是yield后面的book对象
	def process_item(self, item, spider):
		# 以下这种模型不推荐  每传递一个对象 就打开一次文件  对文件操作过于频繁

		# 1.write方法必须要写一个字符串  而不能是其他对象
		# 2.w模式会每一个对象都打开一次文件  覆盖之前的内容
		# with open('book.json','a',encoding='utf-8')as fp:
		#     fp.write(str(item))

		self.fp.write(str(item))
		return item

	# 爬虫结束后执行的
	def close_spider(self, spider):
		self.fp.close()


# 开启多条管道下载
#     定义管道类
#     在setting 开启管道
class DangDangDownloadPipelines:
	def process_item(self, item, spider):
		url = 'http:' + item.get('src')
		filename = '/book/' + item.get('name') + '.jpg'

		urllib.request.urlretrieve(url=url, filename=filename)

		return item


# 加载setting文件
from scrapy.utils.project import get_project_settings

import pymysql
class MysqlPipeline:

	def open_spider(self, spider):
		setting = get_project_settings()
		# DB_HOST = '127.0.0.1'
		# DB_PORT = 3306
		# DB_USER = 'root'
		# DB_PASSWORD = '11111'
		# DB_NAME = 'spider'
		# DB_CHARSET = 'utf-8'

		self.host = setting['DB_HOST']
		self.port = setting['DB_PORT']
		self.user = setting['DB_USER']
		self.password = setting['DB_PASSWORD']
		self.name = setting['DB_NAME']
		self.charset = setting['DB_CHARSET']

		self.connent()

	def content (self):
		self.conn = pymysql.connect(
			host=self.host,
			port=self.port,
			user = self.user,
			password=self.password,
			db=self.name,
			charset=self.charset
		)

		self.corsor = self.conn.cursor()


	def process_item(self, item,spider):
		sql = 'insert into book(name,scr) values ("{}","{}")'.format(item['name'],item['src'])
		self.corsor.execute(sql)

		self.conn.commit()
		return item


	def close_spider(self, spider):
		self.cursor.close()
		self.conn.close()