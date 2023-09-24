# if、else、elif的语法结构：if 条件：
# 四个空格缩进 具体执行内容(if的第二行一定要有缩进，否则会报错，四个空格是一个习惯性写法，不是四个也可运行但不规范)
# else:
# 四个空格缩进 具体执行内容(同缩进)

age = 88
if age >=90:
    print('优秀')
elif age >=80:
    print('良好')
elif age >=60:
    print('及格')
else:
    print("不及格")
# if-elif-else结构中不含其他编程语言的大括号，
# 因而要注意缩进要有并且要正确地缩进，否则逻辑会发生错误！


# 小demo  数读入的内容默认是字符串(string)类型的，我们要先做一步强制类型转换为整型(int)，而后与int型数值进行比较，否则会报错。(python不支持int和string直接比较！
socre = int(input('请输入你的成绩'))
if socre >=90:
    print('优秀')
elif socre >=80:
    print('良好')
elif socre >=60:
    print('及格')
else:
    print("不及格")