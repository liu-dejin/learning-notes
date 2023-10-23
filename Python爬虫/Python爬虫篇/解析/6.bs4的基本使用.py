from bs4 import BeautifulSoup

# 解析本地文件
# 默认打开是jbk ， 需要制定编码
soup = BeautifulSoup(open('bs4基本使用.html',encoding='utf-8'),'lxml')
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
print(soup.find('a',title='a2'))	#根据title的值找到对应标签对象
print(soup.find('a',class_ = 'a1'))  #根据class的值找到对应的标签  class需要添加下划线
# find_all`
print(soup.find_all('a'))	#返回的是一个列表返回的所有a变迁
print(soup.find_all(['a','span']))	#如果想获取多个数据,需在find_all的参数中添加列表的数据
print(soup.find_all('li',limit=2))
# select