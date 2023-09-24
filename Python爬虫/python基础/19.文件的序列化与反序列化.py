# 文件的序列化和反序列化
 
# 默认情况下，只能直接将字符串写入文件，列表、元组、字典等对象无法写入文件：
fp = open('demo_file/test3.txt','w')
fp.write('hello world')
fp.close()
name_list = ['张三','李四']
fp_1 = open('demo_file/test4.txt','w')
# fp_1.write(name_list) 这句话就会报错，因为无法直接向文件写入列表对象，
# 只能先进行序列化，而后写入
fp_1.close()
 
# 序列化：对象 - - - > 字节序列(json字符串)
 
# 序列化有两种方式：
# (1) dumps() 函数 法
# 首先创建一个文件，并定义一个列表：
fp_2 = open('demo_file/test5.txt','w')
name_list = ['zhangsan','lisi']
# 导入json模块到python文件：
import  json
# 进行序列化：使用json库的dumps()函数进行对象序列化：
names = json.dumps(name_list)
fp_2.write(names)
fp_2.close()
 
# (2) dump() 函数 法
# 它与dumps()的区别在于
# dump()函数在完成序列化的同时，会指定目标文件，并完成写入操作
# 类似于一步完成dumps()的两个操作：
fp_3 = open('demo_file/test6.txt','w')
# 这里可以看出，传入的参数多了一个文件对象，也即这就是指定的目标文件，序列化的内容会直接写进去：
json.dump(name_list,fp_3)
fp_3.close()
 
fp_4 = open('demo_file/test6.txt','r')
# 此时执行读取，它的结果是一个字符串类型：
content = fp_4.read()
print(type(content))
print(content)
fp_4.close()
# 但是我们的目的是要读出一个列表/元组/字典对象，因此需要做反序列化：
 
# 反序列化：字节序列 (json字符串)- - - > 对象
 
# 反序列化也有两种方法：
# (1) loads() 函数 法
fp_5 = open('demo_file/test6.txt','r')
content = fp_5.read()
# 调用json库中的loads()函数，传入被序列化的字符串变量，返回反序列化的json字符串：
import json
content = json.loads(content)
print(type(content))
print(content)
fp_5.close()
 
# (2) load()函数 法：
# 此法与dumps和dump的区别一样，也是实现了两步合成一步
# 即读取字符串与字符串转json对象(列表、元组、字典)合并在一步：
fp_6 = open('demo_file/test6.txt','r')
# 调用json库中的load()函数，同时完成读取+转换json对象：
result = json.load(fp_6)
print(result)
print(type(result))
fp_6.close()