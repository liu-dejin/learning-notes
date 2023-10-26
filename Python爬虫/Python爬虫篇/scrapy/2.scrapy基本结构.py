# 1.scrapy项目的结构
# spiders
		# __init__.py
		# 自定义的爬虫文件.py ‐‐‐》由我们自己创建，是实现爬虫核心功能的文件 **********************
# __init__.py
# items.py ‐‐‐》定义数据结构的地方，是一自scrapy.Item的类
# middlewares.py ‐‐‐》中间件 代理
# pipelines.py ‐‐‐》管道文件，里面只有一个类，用于处理下载数据的后续处理
# 默认是300优先级，值越小优先级越高（1‐1000）
# settings.py ‐‐‐》配置文件 比如：是否遵守robots协议，User‐Agent定义等

# 2.response的属性和方法
# 字符串    response.text
# 二进制    response.body
# xpath语法来解析response内的内容 response.xpath
# 提取seletor对象的data属性值	response.seletor
# 提取seletor列表的第一个值	response.seletor.first()