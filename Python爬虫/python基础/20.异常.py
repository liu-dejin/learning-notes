# fp = open('text.txt' , 'r')
# fp.read()
# fp.close()


#  异常处理：由于代码错误后，默认弹出的错误不利于用户理解，
#  因而在写代码时，对于可能出错的部分，做异常处理，使得弹
#  出的错误能被用户理解为上上策。

# 异常处理格式
# try:
#   可能出现异常的代码
# except 异常的类型
#   友好的提示

try:
    fp = open('text.txt' , 'r')
    fp.read() 
except FileExistsError:
    print('系统正在升级,请稍后重试...')