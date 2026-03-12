
# 私有属性和私有方法不能继承：
#     私有属性和私有方法只能在当前类内部使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性
        
    def run(self):
        print("Person父类中的run")

    def __smoke(self):
        print("Person父类会smoke")

class Boy(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex

    def sleep(self):
        print("Boy子类中的sleep")
        # print(self.__age)  # AttributeError: 'Boy' object has no attribute '_Boy__age'

boy = Boy("zzz", 20, '男')
print(boy.name)

# 类外部不可以直接使用私有属性
# print(boy.age)  # AttributeError: 'Boy' object has no attribute 'age'

# 子类不能访问父类的私有属性和私有方法
boy.run()
boy.sleep()  # 执行print(self.__age)会报错
# boy.__smoke()  # AttributeError: 'Boy' object has no attribute '__smoke'
'''
zzz
Person父类中的run
Boy子类中的sleep
'''
