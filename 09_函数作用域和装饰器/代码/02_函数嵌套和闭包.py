
# 函数名称：既是函数名，也是指向该函数的变量
#          只要是指向该函数，就可以调用该函数

def f1():
    print('f1')
f1()

f2 = f1
f2()

print()



# 函数嵌套
def func():
    def fn():
        print('fn函数')

    return fn  # 函数声明和函数调用才会在函数名后面加"()"

# fn()  # NameError: name 'fn' is not defined. Did you mean: 'func'?
# 函数fn在函数func中定义，fn只能在func中调用，fn不能在func外调用

fn22 = func()   # fn22 = func() = fn()
fn22()  # 调用fn22()实际上调用的是fn()，打印'fn函数'

print(fn22.__name__)    # fn  打印真实指向的函数，说明fn22真实指向的是fn




# 闭包：函数嵌套，且返回内部函数 就会形成闭包  (了解即可)
#       函数作用域中的变量x=10不会被释放

def func3():
    x = 10
    def func4():
        nonlocal x  # 声明x为非局部变量，即x=10不会被释放
        x += 1

        print('func4 x:', x)

    return func4


f = func3()     # f = func4 给变量f赋值为func3，即f指向func3的返回值函数func4，此时f其实是一个函数类型
f()  
f()

