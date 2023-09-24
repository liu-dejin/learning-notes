# python文件操作
#
# 创建/打开一个文件：test.txt
# 格式为：open(文件的路径；文件的模式)
# 模式有：w 可写   r 可读  a 追加
fp = open('demo_file/test.txt','w')
 
# 文件的关闭
# 执行打开、读写操作后要及时关闭文件，释放内存！
fp.close()
 
# 文件的读写
 
# 向文件内写入内容：
# 格式为 文件对象.write('内容')
fp_w = open('demo_file/test1.txt', 'w')
fp_w.write('hello,world\n' * 5)
fp_w.close()
 
# 在w 写入模式下，每一次打开后，写入的位置都是开头，也即会覆盖之前的内容
# 在a 追加模式下，每一次会紧接着上一次写入的内容，不会覆盖：
fp_a = open('demo_file/test2.txt', 'a')
fp_a.write('hello\n' * 5)
fp_a.close()

# ，当文件在路径下不存在的时候，运行'w'写入模式时会自动创建文件并定为写入模式；
# 'a'追加模式下，我们才可以每一次接着前一次的结尾写入，否则'w'模式下每一次都会覆盖前一次写入的内容！