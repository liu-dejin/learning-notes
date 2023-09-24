# 字典高级
 
# 定义一个字典：
person = {'name' : '跳探戈的小龙虾', 'age' : 20}
 
# 字典高级：查询
 
# (1). 字典变量名['key'] 查询元素
print(person['name'])
print(person['age'])
# 当访问不存在的'key'值时，出现的情况是会报错：
# print(person['sex'] 会报错 key error
 
# (2). get()函数 查询元素
print(person.get('name'))
print(person.get('age'))
 
# 字典高级：修改
 
# 例如修改上例中 'name' 键的值为 '张三'
person['name'] = '张三'
print(person['name'])
 
# 字典高级：添加
 
# 例如添加一个新的 键值对：'sex' 'nan'
person['sex'] = 'nan'
# 添加的格式与修改相同，只是此时 键 key 是不存在的，
# 因此会新建该键值对，如果该键存在，那就是修改操作
 
# 字典高级：删除
 
# (1) del 关键字删除：删除字典中指定的某一个元素
del person['sex']
print(person)
 
# (2) del 关键字删除：删除整个字典，包括字典对象本身
del person
# print(person) # 这时打印会报错，因为person字典已经不存在了
 
# (3) clear 清空字典内容，但是保留字典对象
person = {'name' : '跳探戈的小龙虾', 'age' : 20}
person.clear()
print(person) # 此时打印的结果只有一个 {}，因为内容已被清空！但不会报错
 
# 字典高级：遍历
 
# (1) 遍历字典的key
# 字典.keys() 方法，获取字典所有的key值，而后用
# for循环即可，用一个临时变量进行遍历
person = {'name' : '跳探戈的小龙虾', 'age' : 20}
for key in person.keys():
    print(key)
 
# (2) 遍历字典的value
# 字典.values() 方法，获取字典所有的value值，而后用
# for循环即可，用一个临时变量进行遍历
for value in person.values():
    print(value)
 
# (3) 遍历字典的key和value
# 字典.items() 方法，获取所有的key  value键值对，
# 并且用两个临时变量通过for循环遍历
for key,value in person.items():
    print(key,value)
 
# (4) 遍历字典的项/元素
# 仍然是字典.items() 方法，但是此时只用一个临时变量去循环遍历
# 即可获取字典的每一项，这与上一种的区别在于获取的
# 键值对会用一个()包围，即打印的结果是(key,value)
for item in person.items():
    print(item)


# demo
dic1= {'name' :'ldj','age':16}


print(dic1['name']) #查
print(dic1.get('age')) #查

dic1['sex'] ='男' #增
print(dic1)

del dic1['sex'] #删
print(dic1)
# del dic1 #删
# print(dic1)
# dic1.clear()  #清空字典内容
# print(dic1)

dic2= {'name' :' 嘤嘤嘤','age':14}
for key in dic2.keys(): #遍历key
    print(key)

for volue in dic2.values(): #遍历value
    print(value)
  
for key,value in dic2.items(): #遍历key和value
    print(key,volue)

for item in dic2.items(): #遍历元素/项  (key,value)
    print(item)