import math


# 回调函数： (了解)
#   把函数当作参数传入另一个函数中
import math
def func(a, callback):    # callback = lambda x: math.pow(x)
    print("n:", a)        # 3
    print("callback", callback(a))    # callback(3) = lambda x: math.pow(3)

func(3, lambda x: math.pow(x,2))


def func(a, callback):     # callback是函数做参数
    print("n:", a)
    print("cb:", callback(a))

def cb(a):     # callback是回调函数
    return math.pow(a, 2)
func(3, cb)


# 使用回调函数过滤
def filter_new(cb, list):
    l2 = []
    for i in list:
        if cb(i):
            l2.append(i)
    return l2

n = filter_new(lambda x : x > 0, [1, -2, 3, -4, -5, 7, 6, -9])
print(n)


# sort(key=lambda)
list1 = [
    {'name': '张三', 'age': 18, 'score': 50, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 16, 'score': 88, 'tel': 18866668998, 'sex': '男'},
    {'name': '王五', 'age': 17, 'score': 48, 'tel': 18866667995, 'sex': '女'},
    {'name': '陈一军', 'age': 61, 'score': 59, 'tel': 18866669998, 'sex': '不明'},
    {'name': '陈二军', 'age': 49, 'score': 88, 'tel': 18866669396, 'sex': '男'},
    {'name': '陈三军', 'age': 49, 'score': 61, 'tel': 18866668994, 'sex': '女'}
]
# 需求1：把list1按照age升序
list1.sort(key = lambda d: d['age'])
print(list1)

# 需求2：把list1按照score降序
list1.sort(key = lambda d: d['score'],reverse=True)
print(list1)


# 练习：按照数字升序
list2 = [
    ('张三', 18),
    ('李四', 16),
    ('王五', 17),
    ('陈一军', 61),
    ('陈二军', 49),
    ('陈三军', 48)
]
list2.sort(key=lambda t: t[1], reverse=False)
print(list2)

