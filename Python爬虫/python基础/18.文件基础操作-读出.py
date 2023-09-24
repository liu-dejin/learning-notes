# 读取文件的内容
# read函数是按每字节读取，效率较低
fp_r = open('demo_file/test2.txt', 'r')
content = fp_r.read()
print(content)
fp_r.close()
 
# readline函数是一行一行的读取，但是调用一次只能读取一行：
fp_l = open('demo_file/test2.txt','r')
line = fp_l.readline()
print(line)
fp_l.close()
 
# readlines函数也是按照行来读取，并且可以一次性把所有行都读取到，
# 并返回一个列表的形式：
fp_ls = open('demo_file/test2.txt','r')
lines = fp_ls.readlines()
print(lines)
fp_ls.close()