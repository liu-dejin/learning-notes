from lxml import etree

# xpath解析
# 1.本地文件												etree.parse
# 2.服务器响应的数据	response.read().decode('utf-8')		etree.HTML()


# xpath解析本地文件
tree = etree.parse("xpath的基本使用.html")
print(tree)

# tree.xpath('xpath路径')

# 查找ul下面的li
# li_list = tree.xpath('//body//li')

# 查看有id属性的li标签
# text获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')


# 找到id为l1的li标签 注意引号问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 找到id为l1的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="l1"]/@class')

# 查询id中包含l的li标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查询id的值为l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 查询id为l1和class为c1的li标签
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

li_list = tree.xpath('//ul/li[@id = "l1"]/text() | //ul/li[@id="l2"]/text()')

print(li_list)
print(len(li_list))


