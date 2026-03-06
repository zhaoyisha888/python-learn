

# 生成器 generator (掌握)
#  需要使用next或者for循环来取用里面的数

'''l = [i for i in range(1, 6)]   # 列表推导式 [1, 2, 3, 4, 5] 
d = {f'{i}': i for i in range(1, 6)}  # 字典推导式 {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
print(l,d) 

[] 和 {} 符号都已经使用，还有 () 符号
''' 

# 生成器表达式(表达式 for 变量 in 可迭代对象)
nums = (i for i in range(1, 4))

print(nums)  # <generator object <genexpr> at 0x000002278F9DF2A0>  生成器对象
# print(list(nums))   # 一般不推荐强转 [1, 2, 3]

# 生成器不会占用很大的内存空间，只有在使用的时候才会生成数据


# 1. next
print(next(nums))  # 1
print(next(nums))  # 2
# print(next(nums))  # 3
# print(next(nums))   # StopIteration 停止迭代，没有更多元素了

# 2. for
# 生成器对象数字拿完就没了，如果上面的next()拿完了生成器对象里的数字，for循环就没有输出了
for i in nums:
    print(i)   # 注释上面的最后一个next()，返回3  


print('*' * 100)


# 生成器函数:
#   1. 函数内部要有 yield
#   2. 需要用next来调用
#   3. 每个next都会在yield处暂停
#   4. yield 会暂停,不会结束  可以返回值,类似return
def fn():
    print('我是fn,看看会不会执行')
    # yield        # 加上yield, , 普通函数就会变成生成器，无法直接调用
    yield 888
    print('我在yield后面，看看会不会执行')
    yield 999

# fn()
gen = fn()   # 生成器对象
# next(gen)    # 我是fn,看看会不会执行

print(gen)   # <generator object fn at 0x000001E173764C40>  fn是生成器对象

print(next(gen))  
'''
我是fn,看看会不会执行
888
'''

print(next(gen))   # 每个next都会在yield处暂停
'''
我是fn,看看会不会执行
888
我在yield后面，看看会不会执行
999
'''


print('*' * 100)


# 示例:
def gen():
    g = (i for i in range(1, 10**100))

    for i in g:
        # 一个个返回值, 不会退出函数
        yield i   # 返回值/暂停


g = gen()
print(g) 
print(next(g))    # 1
print(next(g))    # 2
print(next(g))    # 3
print()



# 练习
# 1.请写一个生成器函数, 得到前20个斐波那契数 (难度:*****)
# 斐波那契数列如下：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
#                 a, b 
#                    a, b
#                       a, b
#                          a, b
#    提示:使用while True, 通过调用n次next来获取前20个数
import time


def fib():
    a = 0     # 初始值
    b = 1     # 初始值
    while True:   
        a, b = b, a + b
        yield a    # 无限循环返回值

gen = fib()
for i in gen:
    print(i, end=' ')
    time.sleep(0.1)



