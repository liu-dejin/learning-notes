# 普通输出
print("故事里的小黄花")

# 格式化输出
# scrapy框架会使用   将爬取的内容存入 Excel、MySQL、Redis

age = 20
name = 'Lobster'
 
# 格式化输出时，%s 代表字符串，%d 代表数字，其他的数据类型的格式化输出爬虫中一般不使用，
# 不做介绍。格式化输出的格式如下：
# 在需要放置输出变量的位置根据类型放置对应的符号，之后在print函数引号后面用一个百分号把
# 变量名放入即可，一个变量名时无需加括号，多个变量名用一个括号按顺序括起来，逗号隔开
print('昵称：%s,年龄：%d' % (name,age))

# input()函数内的字符串会作为读入的提示语句显示在控制台
password = input('请输入你的银行卡密码')
print(password)

# 小demo
password1 =input('请输入你的银行密码')
print('我的银行卡密码是:%s'%password1)

