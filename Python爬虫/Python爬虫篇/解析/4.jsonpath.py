# jsonpath 只能解析本地文件

import json
import jsonpath

obj = json.load(open('store.json','r',encoding='utf-8'))

# 书店所有书的作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
#
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下的所有元素
# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# store 下的所有钱
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj,'$..book[3]')
# print(book)

# 最后一本书
# end_book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(end_book)

# 前两本书
# book_list = jsonpath.jsonpath(obj,'$..book[0,1]')
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)

#
# 过滤出包含版本号的书
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book_list)

# 价格超过10块钱的书
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)')
print(book_list)


