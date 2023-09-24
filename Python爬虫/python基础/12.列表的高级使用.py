# 列表高级：添加
 
# 1. append  追加，在列表的最后一位添加一个对象/数据
food_list = ['apple', 'banana']
print(food_list)
food_list.append('cock')
print(food_list)
 
# 2. insert  插入，两个参数，第一个参数代表想要插入的下标位置，
# 第二个参数代表你要插入的对象/数据
char_list = ['a','c','d']
print(char_list)
char_list.insert(1,'b')
print(char_list) # a b c d
 
# 3. extend  继承，传入的是一个列表，把传入的列表整个插入到
# 调用extend()函数的列表的末尾：
num_list = [1,2,3]
num_list2 = [4,5,6]
num_list.extend(num_list2)
print(num_list)
 
# 列表高级：修改
 
# 将列表中的元素的值修改
# 实现的方法类似于其他编程语言中给数组某一位赋一个新的值覆盖旧值：
city_list = ['Beijing','Shanghai','Shenzhen','Henan']
print(city_list)
# 假设想要修改第三位，Shenzhen，其索引值是2：
city_list[2] = 'Changchun'
print(city_list)
 
# 列表高级：查询
 
# 判断已知数据是否在列表内：
# 用关键字：in或者not in即可，in/not in的前面是待查询的元素，in/not in后面是一个列表
# 1. in代表待查询的元素在列表中：
# 存在时返回true，不存在返回false
food_list = ['apple', 'banana','cock']
 
food = 'apple'
 
if food in food_list:
    print('存在')
else:
    print('不存在')
 
# 2. not in也是查询的关键字，代表待查询的元素不在列表中：
# 不存在时返回true，存在时返回false
ball_list = ['Basketball','Football']
 
ball = 'pingpang'
 
if ball not in ball_list:
    print('不存在')
else:
    print('存在')
 
# 列表高级：删除
 
# 1. 根据下标删除列表中的元素
a_list = [1,2,3,4,5]
print(a_list)
# 例如要删除下标为2的元素3，使用关键字del 加列表 加对应索引：
del a_list[2]
print(a_list)
 
# 2. 删除列表的最后一位元素，使用关键字
b_list = [1,2,3,4,5]
print(b_list)
# 使用pop()函数能够删除最后一位元素：
b_list.pop()
print(b_list)
 
# 3. 根据元素的值，删除元素
c_list = [1,2,3,4,5]
print(c_list)
# 例如想要删除元素值为3的元素，使用remove()函数即可，传入值：
c_list.remove(3)
print(c_list) # 打印结果：1 2 4 5，如果是索引，那应是 1 2 3 5