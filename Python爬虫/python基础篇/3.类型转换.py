# 类型转换
# int(x) 将x转换为一个整数
# float(x) 将x转换为一个浮点数
# str(x) 将对象 x 转换为字符串
# bool(x) 将对象x转换成为布尔值

# 1.其他类型转整型(int)
a = '123'
print(type(a))
b = int(a)
print(type(b))
print(b)
 
# float --> int
c = 1.63
print(type(c))
# float转成整数，会返回小数点前的整数，不涉及四舍五入
d = int(c)
print(type(d))
print(d)
 
# boolean --> int
# True 代表 1，False 代表 0
e = True
print(type(e))
f = int(e)
print(type(f))
print(f)
g = False
h = int(g)
print(h)
#  在float转int过程中，不涉及四舍五入，只是单单的把小数点后面的数据抹掉了(丢失精度)
#  布尔型变量True转int后的值是 1，False转int后的值是 0
# 以下两种情况将会转换失败
'''
123.456 和 12ab 字符串，都包含非法字符，不能被转换成为整数，会报错
print(int("123.456"))
print(int("12ab"))
'''

# 2.其他类型转浮点数(float)
a = '12.34'
print(type(a))
b = float(a)
print(type(b))
print(b)
# a = '12.34' 的变量a，是不能直接由字符串转成整型int类型的，只能直接转浮点数float(即转int的字符串本身不能包含特殊字符)
 
c = 666
print(type(c))
d = float(c)
print(type(d))
print(d)

# 3.其他类型转字符串(string)
# int -> string
a = 80
print(type(a))
b = str(a)
print(type(b))
print(b)
 
# float -> string
c = 1.2
print(type(c))
d = str(c)
print(type(d))
print(d)
 
# boolean -> string
e = True
print(type(e))
f = str(e)
print(type(f))
print(f)
# 布尔型转string的时候，不是转成0或1，而是转成字符串'False'或'True'

# 4.其他类型转布尔型(boolean)
# int -> boolean
a = 1
print(type(a))
b = bool(a)
print(type(b))
print(b)
# 非0的整数都是true，包括负整数和正整数
 
c = 0
print(type(c))
d = bool(c)
print(type(d))
print(d)
 
e = -1
print(type(e))
f = bool(e)
print(type(f))
print(f)
 
# float -> boolean
g = 1.0
print(type(g))
h = bool(g)
print(type(h))
print(h)
 
# 0.0相当于0，所以0.0是false，除了0.0的浮点数无论正负都是false
 
i = 0.0
print(type(i))
j = bool(i)
print(type(j))
print(j)
 
# string -> boolean
# 只要字符串有内容，都是True(内容甚至包括空格)，但是没有内容的，就是False
k = '跳探戈的小龙虾'
print(type(k))
l = bool(k)
print(type(l))
print(l)
 
# 这个就是包含空格，运行结果是True
m = ' '
print(type(m))
n = bool(m)
print(type(n))
print(n)
 
# list -> boolean
# 只要列表有数据，就是True
o = ['a','b','c']
print(type(o))
p = bool(o)
print(type(o))
print(p)
 
# 空列表是False
q = []
print(type(q))
r = bool(q)
print(type(r))
print(r)
 
# tuple -> boolean
# 只要元组有数据，就是True
s = ('a','b')
print(type(s))
t = bool(s)
print(type(t))
print(t)
 
# 空元组是False
u = ()
print(type(u))
v = bool(u)
print(type(v))
print(v)
 
# dict -> boolean
# 只要字典有数据，就是True
w = {'a' : '1','b' : '2'}
print(type(w))
x = bool(w)
print(type(x))
print(x)
 
# 空字典是False
y = {'a' : '1','b' : '2'}
print(type(y))
z = bool(y)
print(type(z))
print(z)