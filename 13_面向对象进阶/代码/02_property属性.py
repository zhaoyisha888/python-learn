
# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# 一般用于返回快速计算的值和内部的私有属性
# @property  # (掌握)  函数可以当属性用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter：用来获取值
    @property  # 通过把age变成属性方式获取值
    def age(self):  # 被@property修饰，不能有参数
        return self.__age

    # setter  用来修改值
    @age.setter   # 通过把age变成属性方式修改值
    def age(self, new_age):     # 可以有参数
        if self.__age  <  new_age:
            self.__age = new_age

# 对象
p = Person("张三",23)

print(p.age)  # 23   实际上调用的是函数age
# 如果注释@property
# <bound method Person.age of <__main__.Person object at 0x0000012822128A50>>

p.age = 60  # setter功能
print(p.age)  # 60
# 如果注释@age.setter和它修饰的函数
# AttributeError: property 'age' of 'Person' object has no setter