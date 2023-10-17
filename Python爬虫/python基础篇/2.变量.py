# 1.变量的定义
# 重复的值写起来和修改都很复杂
print('今天天气很好,又下雨了')
print('今天天气很好,又下雨了')
print('今天天气很好,又下雨了')
print('今天天气很好,又下雨了')
# 用变量来提高编程效率

# 变量的格式: 变量名=变量值

weather = '今天的天气很好,晴天了 '

print(weather)
print(weather)
print(weather)
print(weather)

# 应用场景

img = 'kis2.cn'
print(img)

# 2.变量的数据类型
# numbers
# int float 
# boolean
# true False
# string 
# list 
# tuple
# dictionary

money = 5000
money1 = 1.2

# boolean 布尔
# 流程控制语句会用到
sex = True
gender = False

# string 字符串  单引号或双引号
s = '苍茫的天涯是我的爱'
s1 = "滴答滴答"
# 双引号成对出现
# s2 = '哈哈哈''
# s3 = ''哈哈哈'

# 单引号和双引号嵌套
s4 = '"嘤嘤嘤"'
print(s4)
# '''' """" 不可以

#列表 元组 字典
# list  应用场景:当获取到多个数据,我们可以将他们添加到列表,然后直接访问
name_list = ['周杰伦','陈奕迅']
print(name_list)

# tuple 元组
age_tuple = (18,19,29)
print(age_tuple)

# dict 字典  应用场景:scrapy框架使用
# 格式: 变量名 = {key:value,key1:value1}
person = {'name':'红玫瑰','age':18}
print(person)

# 3.查看数据类型  变量没有类型,数据才有类型
# type查看变量存储的数据类型
a = "111"
print( type(a))

# 4.变量的命名规范  见名知意 驼峰命名
# 字母,下划线,数字组成,数字不可开头
# 严格区分大小写 
# 不能使用关键字