
# 文件操作:
#  1.打开文件
#  2.操作文件(读取read / 写入write)
#  3.关闭文件

# 1.打开文件
# open(file, mode='r')  mode默认值为r
#   file: 打开的文件路径
#   mode:
#     r : 只读read, 如果文件不存在则报错  非二进制读涉及中文需要 encoding='utf-8
#     rb: 只读二进制, 如果文件不存在则报错
#
#     w : 清空写write, 如果文件不存在会自动创建  非二进制清空写涉及中文需要 encoding='utf-8
#     wb: 清空写二进制, 如果文件不存在会自动创建
#     a : 追加写append, 如果文件不存在会自动创建  非二进制追加写涉及中文需要 encoding='utf-8
#     ab: 追加写二进制, 如果文件不存在会自动创建


# 文件句柄, 文件对象
# 读取
# 文件不存在时会报错 FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'

# fp= open('a.txt', 'r', encoding='utf-8')   
'''
非二进制读取的需要设置编码 
否则UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 26: illegal multibyte sequence
'''
fp = open('a.txt', 'rb')  # 以二进制读取文件没有 编码参数

# 现在创建一个a.txt再执行打开语句

# 一次性读取所有内容，可能会占用大量内存
print(fp.read())  # b'haskjsckn\r\nhello world\r\n\xe4\xb8\xad\xe5\x9b\xbd'  二进制读取的内容是bytes类型
'''
haskjsckn
hello world
中国
'''


# 读取一行内容，会一直往下读行，直到文件末尾
# print(fp.readline())   # haskjsckn
# print(fp.readline())   # hello world

# 读取所有行，返回一个列表，每行是列表的一个元素 
# print(fp.readlines())  # ['haskjsckn\n', 'hello world']

# 一次从文件中读取n个字符，重复执行会继续往下读，直到文件末尾
# print(fp.read(3))  # has
# print(fp.read(3))  # kjs


fp.close()  # 关闭文件
print()



# 写
# 如果没有文件就创建文件，有文件就清空旧文件再写
# 写的时候读取文件会报错，需要关闭文件再读

# 清空写 'w'
# fp = open('b.txt', 'w', encoding='utf-8')   
# fp.write('hello 船长, i am a file named b.txt!') 
# print(fp.read())  # io.UnsupportedOperation: not readable 只能写不能读，除非关闭之后再读

# fp = open('b.txt', 'wb')  
# fp.write('hello 旅行者, i am a file named b.txt!'.encode('utf-8'))  


# 追加写 'a'
# fp = open('b.txt', 'a', encoding='utf-8')  
# fp.write('\nhello 旅行者, welcome to my train!\n')

fp = open('b.txt', 'ab')  
fp.write('\nhello 开拓者!\n'.encode())  # 二进制写入需要编码，默认utf-8编码

fp.close()  # 关闭文件


# with-as : 会自动关闭文件(就算中途读写出错了也会自动关闭文件)
with open('b.txt', 'a', encoding='utf-8') as fp:
    fp.write('\n星期天小鸟太可爱了!\n')

# print(fp.read())  # ValueError: I/O operation on closed file.说明已经关闭了文件，需要重新打开才能读

with open('b.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())  # 之前写入的内容都在文件里了
'''
hello 旅行者, i am a file named b.txt!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 旅行者, welcome to my train!

hello 开拓者!

hello 开拓者!

星期天小鸟太可爱了!

hello 开拓者!

星期天小鸟太可爱了!

hello 开拓者!

星期天小鸟太可爱了!

hello 开拓者!

星期天小鸟太可爱了!

hello 开拓者!

星期天小鸟太可爱了!

'''