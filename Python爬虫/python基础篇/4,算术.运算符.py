# 算术运算符
a = 3
b = 2
 
# 加法
print(a +  b)
 
# 减法
print(a - b)
 
# 乘法
print(a * b)
 
# 除法 默认是保留小数
print(a / b)
 
# 取整
print(a // b)
 
# 取余
print(a % b)
 
# 幂运算
print(a ** b)
 
# 字符串加法：字符串拼接
c = '123'
d = '456'
print(c + d)
 
# 在Python中，字符串做加法时，加号两端必须两端都是字符串，若只有一端是字符串，则会报错：
e = '123'
f = 456
#print(e + f) # 此行会报错
print(e + str(f)) # 这是出现这种情况的处理策略：先转成str再来
 
# 在python中，还支持字符串乘法：
g = 'hello world '
print(g * 3)

# 首先是两个字符串相加,相当于做了字符串拼接,不过这一点在其他编程语言中也是如此。python不支持string类型与int类型直接做加法,这样做会报错