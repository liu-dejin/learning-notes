# 1.创建爬虫项目	scrapy startproject scrapy_baidu
# 	不能数字开头不能包含中文

# 2.创建爬虫文件
# 	进入spider文件夹
# 	cd 项目名字	项目名字	spiders
# 	cd \scrapy_baidu\scrapy_baidu\spiders

#  	scrapy 爬虫文件的名字  要爬取的网页
# 	scrapy genspider baidu www.baidu.com
# 	一般不用添加https		start_urls是根据allowed_domains修改的,如果添加了url  弄巧成拙

# 3.运行爬虫代码
# 	scrapy crawl 爬虫的名字
# 	scrapy crawl baidu
