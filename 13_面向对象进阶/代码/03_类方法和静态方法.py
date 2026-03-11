
# 类：
#    属性：类属性，对象属性，私有属性
#    方法：对象方法（公有方法/成员方法），私有方法， 类方法，静态方法

class Person:
    # 类属性
    age = 3

    def __init__(self, name, age):
        # 对象属性
        self.name = name
        self.__age = age  # 私有属性

    # 对象方法/成员方法/公有方法
    def run(self):
        print("run")
        print(self.name, self.__age)
        print(self.age, Person.age)
        self.__sleep()

    # 私有方法
    def __sleep(self):
        print("sleep")

    # 类方法: (掌握)  一般此方法会独立于类中的其他方法
    # @classmethod
    #    1.类方法可以用类名来调用（推荐），也可以用对象来调用(不推荐)
    #    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
    #    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法
    #      cls可以调用类属性，其他类方法，静态方法
    @classmethod
    def eat(cls):   # cls: class
        print("eat")
        print(cls == Person)
        print(cls.age)

    # 静态方法:（了解）
    # @staticmethod
    #    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
    #    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法
    @staticmethod
    def game():
        print("静态方法")

# 对象
# p = Person("zzz", 36)
# p.run()

Person.eat()
Person.game()

# 之前经常遇到的类方法,建议点进去看一眼原函数怎么写的
import datetime
dt = datetime.datetime(2026, 8, 1)
print(dt.hour)   # hour方法被 @property修饰 为属性hour，值为只读
datetime.datetime.fromtimestamp()  # fromtimestamp类方法被@classmethod修饰，可以直接用类名datetime来调用








