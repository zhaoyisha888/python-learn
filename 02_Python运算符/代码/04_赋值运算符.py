

# 赋值运算符 =
#    等号右边先运算再赋值给左边
a = 10 + 2
print(a)



# 复合运算符： 算术运算符 + 赋值运算符
a = b = 100
a += 1  # 等价于 a = a + 1
b %= 4  # 等价于 b = b % 4 取模运算
print(a, b)  # 101 0


# Python中一般都是二元运算符。没有一元运算符a++, 没有三目运算符 ?:
# 一元运算符： 只有一个操作数的运算符，如：++ -- 等, 
# a++  # SyntaxError: invalid syntax  无效的运算符

# 三目运算符： 三个操作数，如：a ? b : c  （C语言中）
# a ? b : c  # SyntaxError: invalid syntax



