
# 练习
# 创建一个工具类Number，其中：
# 类属性：num  初始值为10
# 类方法：add_num(cls)  让num加1
#        sub_num(cls)  让num减1
#        mul_num(cls, n) 让num乘n
#        div_num(cls, n) 让num除n
# 静态方法：
#        add(x, y) : 求x+y的结果并返回
#        sub(x, y) : 求x-y的结果并返回
#
#  不创建对象，分别调用这些方法，然后打印num

class Number:
    # 类属性
    num = 10

    def __init__(self):
        # 对象属性
        pass

    # 类方法
    @ classmethod
    def add_num(cls):
        # add_num(cls) 让num加1
        cls.num += 1

    @ classmethod
    def sub_num(cls):
        # sub_num(cls)  让num减1
        cls.num -= 1

    @ classmethod
    def mul_num(cls, n):
        # mul_num(cls, n) 让num乘n
        cls.num *= n

    @ classmethod
    def div_num(cls, n):
        # div_num(cls, n) 让num除n
        cls.num /= n

    # 静态方法
    @ staticmethod
    def add(x, y):
        # add(x, y): 求x + y的结果并返回
        return x+y

    @staticmethod
    def sub(x, y):
        # sub(x, y) : 求x-y的结果并返回
        return x - y


Number.add_num()
print(Number.num) # 11

Number.sub_num()
print(Number.num) # 10

Number.mul_num(6) # 60
print(Number.num)

Number.div_num(2) #30.0
print(Number.num)

print(Number.add(1,5)) # 6

print(Number.sub(5,2)) # 3

