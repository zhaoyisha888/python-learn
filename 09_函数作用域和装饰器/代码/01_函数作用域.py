
# 作用域：变量起作用的范围
#   函数有作用域

# 全局变量：全局作用域
a = 10
def fn():
    # 局部变量：局部作用域，退出函数（作用域）后会自动释放变量占用的内存
    b = 20
    print('a:', a)
    print('b:', b)
fn()

# 不能使用函数内部定义的局部变量
# print(b)   # NameError: name 'b' is not defined

# if/whlie/for循环 语句没有作用域
# if True:
#     c = 100
# print('c:', c)
#
# i = 1
# while i:
#     d = 400
#     i -= 1
# print('d:',d)



# 函数嵌套
# 内建作用域 B： Built-in，整个python环境都能使用
# 全局作用域 G： Global
# 函数作用域 E： EnClosing
# 局部作用域 L： Local

x = 3     # Global
def func1():
    y = 4      # EnClosing 闭包，嵌套中间的变量

    def func2():
        z = 5      # Local


# 关键字： global，nonlocal

m = 6  # 全局变量
def f1():
    m = 4  # 局部变量
    print('函数内部 m:', m)
f1()
print('函数外面的 m:', m)

# global
m = 6
def f1():
    global m  # 声明全局变量
    m = 4
    print('函数内部 m:', m)
f1()
print('函数外面的 m:', m)

print('----------------------------------------------------------------------------------------------------------------')

# nonlocal ： 非局部变量，函数嵌套才使用
A = 6   # 全局变量
def f1():
    A = 4   # 函数作用域
    def f2():
        # global A  # 声明全局变量
        nonlocal A  # 声明非局部变量, 但也不是全局变量。 从本函数往上找，找到第一个A变量的值
        # A = 5       # 局部变量

        print('f2的 A:', A)         # global A = 6, nonlocal A = 4, A = 5
       
    f2()
    print('f1的 A:', A)

f1()   
print('函数外的 A:', A)
