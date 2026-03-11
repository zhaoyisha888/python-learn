

# self:
#   1.不是关键字, 只是一个形参，但是建议写self, 不需要给self传值
#   2.self是指向当前类的对象（哪个对象调用函数，则该函数中的self就是这个对象）
#   3.作用是让你可以在函数中调用类中的其他属性或方法

class Dog:
    def __init__(self,name):
        self.name = name
        print('__init__函数中的self:', id(self))

    def eat(self):
        print('狗喜欢啃骨头')
        print('eat函数中的self:', id(self))

# 创建对象
dog = Dog('旺财')
# print(dog.name)
print("id(dog):", id(dog))  # 查看对象内存地址
dog.eat()
'''
__init__函数中的self: 2489302159120
id(dog): 2489302159120
狗喜欢啃骨头
eat函数中的self: 2489302159120
'''

print('-' * 100)

dog2 = Dog('大黄')
print("id(dog2):", id(dog2))
dog2.eat()
'''
__init__函数中的self: 2489302159440
id(dog2): 2489302159440
狗喜欢啃骨头
eat函数中的self: 2489302159440
'''