
# 转义字符 \ : 让有语义的字符失去语义
# r'' : 让字符串中有语义的字符失去语义
# b'' : 字节
# f'' : f-string

# s = 'D:\Users\python-learn.py'
# print(s)  # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

s = 'D:\\Users\\python-learn.py'  # D:\Users\python-learn.py
print(s)


# 编码和解码
#  编码: encode() 将 字符串 => 二进制
#  解码: decode() 将 二进制 => 字符串
s1 = 'hello 麦当劳'
print(s1.encode('utf-8'))  # b'hello \xe9\xba\xa6\xe5\xbd\x93\xe5\x8a\xb3'
print(s1.encode('gbk'))    # b'hello \xc2\xf3\xb5\xb1\xc0\xcd'
s2 = b'hello \xe9\xba\xa6\xe5\xbd\x93\xe5\x8a\xb3'
s3 = b'hello \xc2\xf3\xb5\xb1\xc0\xcd'
# print(s2.decode('gbk'))   # UnicodeDecodeError: 'gbk' codec can't decode byte 0xb3 in position 14: incomplete multibyte sequence
# print(s3.decode( ) )  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc2 in position 6: invalid continuation byte
print(s2.decode( ),s3.decode('gbk'))  # hello 麦当劳 hello 麦当劳


# ASCII码(了解)
print(ord('a'))  # 97
print(chr(97))  # a
print(chr(97-32))  # A



# strip() : 去除两边的指定字符(默认去除空格)
s = "   hello   "
print(s.strip())  # hello
print("----hello----".strip('-'))  # hello   去除两边的指定符号
print("----hello----".lstrip('-'))  # hello   去除左边的空格
print("----hello----".rstrip('-'))  #    hello  去除右边的空格


# 对齐方式 : 了解
print("hello".center(10, '*'))  # **hello***
# 长度为10，两边填充*，居中对齐
print("hello".ljust(10, '*'))  # hello****   左对齐
print("hello".rjust(10, '*'))  # ****hello   右对齐
print("hello".zfill(10))       # 00000hello 填充0


# 前缀和后缀
print("hello".startswith('he'))  # True   判断是否以he开头
print("hello".endswith('lo'))    # True   判断是否以lo结尾
print("hello".startswith('he', 1))  # False   判断是否以he开头，从索引1开始
print("hello".endswith('lo', 3))    # True   判断是否以lo结尾，从索引3开始