# 逻辑运算符在python中一共有三个，即 与、或、非(取反)
# 逻辑运算符   and   or   not
 
# and 与 , 没错python中的and是手打一个and，不是||
 
print(10 > 20 and 10 > 11)
 
# or   或者
 
print(10 > 20 or 10 > 21)
 
# not  非  取反
 
print(not True)
 
print(not False)
 
a = 36

# 逻辑运算符的短路    优化了逻辑运算符的执行效率
# and 的性能优化：
# 左侧是False，因而右侧不再执行(短路and)
a < 10 and print('hello world')
 
# or的性能优化：
# 左侧是True，因而右侧不再执行(短路or)
a = 38
a > 37 or print('你好世界')

