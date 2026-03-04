
# random: 随机数

# import keyword
# import math
# import time
import random

# random.choice(): 从列表/str中随机取一个元素
money = ["金子","银子","铜钱"]
print(random.choice(money))
print(random.choice("money"))

print(random.choice(range(1,7)))  # 筛子

# random.randint(a, b): 从一个范围随机取一个整数，闭区间
print(random.randint(2, 6))   # 从闭区间[2,6]取值


# random.randrange(a, b, step): 和range类似，可以随机获取一个奇数
print(random.randrange(3, 5))  # [3,5)范围取随机值 3，4
print(random.randrange(3, 10, 2))    # [3,10)范围随机获取一个奇数，3，5，7，9取随机值


# random.random() : 在0~1之间[0,1)随机获取一个小数
print(random.random())
print(1 + random.random() * 9)  # 随机获取1~10之间的一个小数，区间乘法


# random.uniform(3, 5) ： 3~5之间的小数 （了解）
print(random.uniform(3, 5))
print(random.uniform(3, 3))  # [3,3]
'''
def uniform(self, a, b):
    "Get a random number in the range [a, b) or [a, b] depending on rounding."
    return a + (b - a) * self.random()
'''

# random.shuffle(list) : 随机打乱顺序  （了解，机器学习可以用来加噪声，把数据打乱）
n = [1, 2, 3, 4, 5]
random.shuffle(n)  # 打乱列表顺序
print(n)




