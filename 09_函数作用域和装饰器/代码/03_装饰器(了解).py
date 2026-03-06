

# 装饰器：
#   作用是在其他函数的前面或后面添加功能，但是不修改原函数

def swim():
    print('我爱游泳')

def swim2():
    print('先跳个舞')
    swim()
    print('再唱个歌')

# 上面的方式有缺陷：只能给swim添加功能


def run():
    print('我爱跑步')


def run2(fn):
    print('先跳个舞')
    fn()
    print('再唱个歌')

run2(run)
run2(swim)
print('*' * 100)

# 上面方式可以对不同函数进行装饰
# 但还有缺点：调用的方式会发生变化
#    不使用装饰器就调用 run()
#      使用装饰器就调用 run2()


# 标准装饰器
# 定义装饰器
def outer(fn):
    def inner():
        print('先跳个舞')
        fn()   # 实际调用的是传入的sleep()函数
        print('再唱个歌')
    return inner

'''
def sleep():
    print('我爱睡觉')
sleep = outer(sleep)  # 装饰器的原理
print(sleep.__name__)  # inner outer(sleep)返回的是inner函数
sleep()  # 相当于调用inner
'''

@outer   # python标准的装饰器语法
def sleep_new():
    print("我爱睡奇形怪状的觉")

sleep_new()


print('*' * 100)

# 练习：写一个装饰器，计算函数运行的时间
import time
time.time()   # # 获取当前时间
def func_time(fn):
    def inner(*args, **kwargs):   # 通用装饰器，可以接收任意参数
        start_time = time.time()  

        fn(*args, **kwargs)    # 调用被装饰的函数

        end_time = time.time()  
        print(f'函数运行时间为 ：{end_time - start_time}')
    return inner

@func_time
def mysum(x,y):
    s = 0
    for i in range(x, 10**y + 1):
        s += i
    print(s)
    # print(f'1到100的和为: {all_sum}')   # 有文字输出的执行时间会长一点

mysum(1, 5)
