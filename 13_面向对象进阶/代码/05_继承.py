
# 面向对象的4大特征：
#   1. 封装：属性和方法
#   2. 继承：子类可以继承父类的属性和方法
#   3. 多态
#   4. 抽象


# 继承：子类继承父类的属性和方法
#    方便后期维护代码

# 单继承 ： 只有1个父类
class Father(object):
    iq = 140

    def __init__(self, last_name):
        self.last_name = last_name

    def smoke(self):
        print("can smoke")

class Son(Father):
    iq = 180

    def __init__(self, last_name, name):
        super(Son, self).__init__(last_name)
        """
        super() -> same as super(__class__, <first argument>)
        """
        self.name = name

    def study(self):
        print("son study great")

father = Father("Ben")
son = Son("White", "John")
print(son.name)
son.study()
son.smoke()
