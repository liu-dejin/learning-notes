# 字符串常见的函数
 
# 1.获取长度：len()，返回整型
s = 'Lobster'
print(len(s)) #7
 
# 2.获取某个字符在字符串中第一次出现的位置索引值(区分大小写): s.find('')，返回整型
print(s.find('L')) #0
 
# 3.判断是否以某个字符开头、结尾：s.startswith('')，s.endswith('')，返回布尔值
print(s.startswith('O'))
print(s.endswith('r'))
 
# 4.查找某个字符的个数：s.count('')
print(s.count('o'))
 
# 5.替换某个字符：s.replace('','')
print(s.replace('L','l'))
 
# 6.切割字符串：s.split(''),意思是以传入的字符为切割位把原字符串切开，
# 传入这个字符会变成空格
print(s.split('o'))
 
# 7.大小写转换：s.upper()，s.lower()，整个字符串转成大写或小写
print(s.upper())
print(s.lower())
 
# 8. 去掉字符串空格的函数：strip()，能把整个字符串所有空格去掉
s1 = '        Lobster     '
print(len(s1))
print(len(s1.strip())) # 刚好是Lobster的长度7
 
# 9. join()函数，了解即可，是把一个字符串插入
# 到另一个字符串的每一位的后面，而不是简单的拼接，不是很常用：
s2 = 'aaaaaa'
s3 = 'bb'
print(s3.join(s2)) # 输出：abbabbabbabbabba