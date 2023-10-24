from bs4 import BeautifulSoup

# 解析本地文件
# 默认打开是jbk ， 需要制定编码
soup = BeautifulSoup(open('bs4基本使用.html', encoding='utf-8'), 'lxml')
# print(soup)

# bs4基本语法
# 根据标签语法查找节点
# 找到的是第一个符合条件的数据
# print(soup.a)
# attrs 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# find
print(soup.find('a')) #返回的是第一个符合条件的数据
print(soup.find('a',title='s2'))	#根据title的值找到对应标签对象
print(soup.find('a',class_ = 's1'))  #根据class的值找到对应的标签  class需要添加下划线
# find_all`
print(soup.find_all('a'))	#返回的是一个列表返回的所有a变迁
print(soup.find_all(['a','span']))	#如果想获取多个数据,需在find_all的参数中添加列表的数据
print(soup.find_all('li',limit=2))	#limit的作用是查找前几个数据
# select(推荐)
# select 方法返回
# select()返回一个列表，同时和find_all一样返回所有的目标标签
print(soup.select('a'))

# 类选择器(在前端的一种叫法)：可以通过加一个 .类名 来筛选class
print(soup.select('.s1'))

# id选择器(也是前端的一种叫法)：可以通过加一个 #id名 来筛选id
print(soup.select('#s2'))

# 属性选择器：可以通过属性存在与否、属性的具体值来筛选
print(soup.select('li[id]'))  # 这表示查找所有的 li标签 中含有 id 的标签li
print(soup.select('li[id = "l2"]'))  # 这表示查找所有的 li标签 中含有 id 且id的值为l2的标签li

# 层级选择器：
# a.后代选择器：一个空格，查找某个标签的后代，包括儿子、孙子标签
print(soup.select('div li'))

# b.子代选择器：一个大于号，只能查找某个标签的儿子标签，不包括孙子标签
print(soup.select('div > ul > li'))  # 这里写 div > li，则没有内容返回，因为li是div的孙子标签而非子标签

# 多个标签都拿到：
# 在select()中，我们无需用列表的传参表示多个标签，直接以逗号隔开多个标签即可：
print(soup.select('a,li'))

# (4) 获取节点具体的信息的函数
# a.获取节点的内容
# 注意要加一个索引，因为我们的select会返回一个列表，不加索引，就无法处理成字符串
obj = soup.select('#s2')[0]
# 如果标签对象中只有内容，那么string和 get_text()都可以使用
# 但是如果标签对象中有内容也有标签，那么string就无法使用，只能用get_text()
# 推荐使用get_text()
print(obj.get_text())

# b.获取某个具体的节点(标签)的属性
# 首先获取id值是s2的标签
tag = soup.select('#s2')[0]

# 返回这个标签的名字，例如a标签，就返回一个a
print(tag.name)

# 将所有的标签属性以字典的格式返回
print(tag.attrs)

# 获取某个节点的具体某一个属性，原理是可以根据attrs的字典对象特点，
# 用字典对象的get函数，传入键，来获取某一个键值对的值
print(tag.attrs.get('title'))  # 获取id值是s2的标签的title属性

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get("class"))
print(obj.get('class'))
print(obj['class'])

# 处理服务器数据
from bs4 import BeautifulSoup

# soup = BeautifulSoup(content, 'lxml')

# 原理一样,content填前面获取的数据,lxml固定字符



