
# 1.变量 : 可变的量
#   1. 作用是用来存储数据, 为了方便以后使用它做别的运算
#   2. 定义变量时,不需要固定类型(弱类型: 动态数据类型)

# 定义一个变量:
#   将10这个值 赋值 给变量a (a是我们自己取的变量名)
a = 10
print(a)
a = "hello"
print(a)

# 其他定义变量的方式:
a,b = 10,20
print(a,b)     # 10 20

# c = 5, d = 6      # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
c = 5; d = 6       # 正确

c = 5
d = 6     
print(c,d)     # 正确 5 6

c,*d,e = 1,2,3,4,5,6,7,8,9,10
print(c,d,e)     # 1 [2, 3, 4, 5, 6, 7, 8, 9, 10] 10  *d表示剩余的值都赋值给d,为列表类型


# 2. 交换2个变量的值[掌握]
h = 6
k = 8
print(h,k)     # 6 8
# h = k
# k = h
# print(h,k)     # 8 8 ,程序自上而下执行，k赋值给h，h赋值给k，所以h和k的值都是8
h,k = k,h
print(h,k)     # 8 6



# 3. 变量命名规范(标识符): [掌握]
#   1.由数字,字母,下划线组成,且不能以数字开头
#   2.不能使用关键字
#   3.区分大小写
#   4.建议: 如果变量名是由多个单词组成,
#           则使用下划线连接 my_teacher 或 使用小驼峰 myTeacher
#   5.建议: 变量名称 尽量见名知义, 一般使用英文 或 英语单词简写 或 拼音

# 3a = 10    # SyntaxError: invalid decimal literal
# _a = 10     # 正确
# if = 10     # SyntaxError: invalid syntax
age,Age = 18,20
print(age,Age)     # 18 20



# 4. 关键字
# import keyword
# print(keyword.kwlist)   # 关键字列表
# [
#  'False', 'None', 'True', 'and', 'as',
#  'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del',
#  'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 'nonlocal', 'not',
#  'or', 'pass', 'raise', 'return', 'try',
#  'while', 'with', 'yield'
#  ]

import keyword
print(keyword.kwlist)   # 关键字列表

# 能不能使用中文或者字符做变量名，不报错但是最好不要，因为非ASCII字符做变量名不规范
国家,β,δ = "中国","美国","日本"
print(国家,β,δ)     # 中国 美国 日本

'''
判断下面变量命名是否合法,并说明不合法的原因:
	_jielun     合法
	12world      不合法，不能以数字开头
	int          合法，int不是内置关键字，但是是内置函数，不建议使用
	boy_girl     合法
	input        合法，input不是内置关键字，但是是内置函数，不建议使用
	if           不合法,if是内置关键字
    hello&world  不合法，不能使用特殊符号&
    abc@163      不合法，不能使用特殊符号@
'''

# int,input = 10,20
# print(int,input)     # 10 20


# 补充变量

x = y = z = 10   # 不建议使用连续赋值，不利于代码的阅读和维护
x = y = z = [1,2,3]   # 列表是可变类型，赋值给x,y,z的值都在同一个列表，修改x,y,z中的一个，其他两个也会修改
print(x,y,z)     # 10 10 10

# 删除变量，不建议使用，python中有内存回收机制，解释器会自动回收变量，不需要手动删除
# x = 10
# del x
# print(x)     # 删除后不能再次使用，NameError: name 'x' is not defined
