
# 匿名函数： lambda
#   特点：
#       没有名字的函数
#       自带return
#       只表示一些简单的，有返回值的函数
def func1(x):
    return x**2

# => 匿名函数，有返回值，需要变量接收返回值

func2 = lambda x: x ** 2
print(func2(3))

func3 = lambda x, y : x + y
print(func3(1,6))

# 高阶函数
#  map: 映射，对列表做批量处理
'''
map() 把 “可迭代对象” 中的每个元素，逐个传给 “函数” 执行，返回迭代器
映射过程就像 “流水线处理”，逐个处理列表中的元素
map 返回的是迭代器（惰性生成，不直接显示内容），需要转成list/tuple才能看到结果
迭代器的设计初衷是节省内存，遍历完就销毁内部的元素指针，所以无法重复遍历
'''

n = map(lambda x : x ** 3, [1, 2, 3])
print(n)  # <map object at 0x0000025C9552B9D0>
print(list(n))   # [1, 8, 27]
print(tuple(n))    # () 迭代器重复遍历为空

n = map(lambda x, y : x + y, [1, 2, 3], [4, 5, 6])
print(n)  # <map object at 0x000002252C0EBD00>
print(tuple(n))  # (5, 7, 9)
print(list(n))   # [] 同理为空列表

# filter: 过滤,找到符合要求的数据
n = filter(lambda x : x > 0, [1, -2, 3, -4, -5, 7, 6, -9])
print(list(n))  # [1, 3, 7, 6]




