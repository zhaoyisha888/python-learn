
# 数学操作

#    sum(): 求和
#    max()：最大值
#    min(): 最小值
#    round(): 四舍五入
#    abs(): 绝对值
#    pow(): 次方  (了解)  ** 次方

print(sum([1, 2, 2, 3]))
print(sum(range(1,100)))

print(max([1, 2, 2, 3]))

print(min([1, -2, 2, 3]))

print(round(3.1415967, 2))  # 3.15
print(round(3.1415967))     # 3

print(abs(-6))

print(pow(2, 3))


# math: 数学
import math
print(math.e)    # 2.718281828459045
print(math.pi)   # pai = 3.141592653589793
print(math.inf)    # inf 无穷大
print(-math.inf)   # -inf

print(math.sqrt(81))   # 9.0 开平方根
print(math.factorial(5))   # 120 阶乘

print(math.ceil(3.14))   # 4 向上取整，比我大的最小整数
print(math.floor(3.14))  # 3 向下取整，比我小的最大整数

print(math.log(math.e))  # 自然对数 log(e) = ln(e) = 1 底数与真数一样，则对数的值为1
print(math.log10(100))   # 2 对数的值为2，底数为10，真数为100
print(math.log2(2)) # 2 对数的值为2，底数为10，真数为100

print(math.sin(math.pi)) # 三角函数

