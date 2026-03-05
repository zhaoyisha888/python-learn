
# 字符串的基本操作
#  str : 引号包裹的就是字符串 'abc'  "abc" """abc"""

# 1.创建字符串
s1 = "hello world"
s2 = 'hello world'
print(s1, type(s1), s2, type(s2))  # hello world <class 'str'> hello world <class 'str'> 不区分大小写

# 2.索引
print(s1[0])  # h
print(s1[-1])  # d

# 3.长度
print(len(s1)) # 11

# 4. 循环
s = 'abc'

for i in s:
    print(i, end=' ')  # a b c  字符char
print()

for i in range(len(s)):  # 索引
    print(s[i], end=' ')
print()

for i, c in enumerate(s):  # 枚举
    print(i, c)  
print()


# 5.修改字符串: 字符串str是不可变类型
# s = 'abcdefg'
# s[0] = 'A'    # TypeError: 'str' object does not support item assignment
# print(s)  

# 6.切片
s = 'abcdefg'
print(s[1:6:2])  # bdf  [1, 3) 左闭右开, 步长为2
print(s[0:])   # abcdefg  [0, 最后)
print(s[:3])   # abc
print(s[::-1])    # 倒序 gfedcba


# 7.加法
s = 'ABC'
print(id(s))  # 140707676574216
print(s + 'DEF')
print(id(s))  # 140708229289760  地址不变

# 8.乘法(重复)
s = 'ABC'
print(s * 3)  # ABCABCABC

# 9.成员
if 'C' in s:  # True
    print('C in s')

