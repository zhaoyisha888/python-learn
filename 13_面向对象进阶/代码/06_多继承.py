
# 单继承： 只有1个父类
# 多继承： 多个父类 （了解）

# 2个父类： 父亲，母亲
# 1个子类： 儿子


# 父类
class Father:
    def __init__(self,name):
        self.name = name
    def smoke(self):
        print("会抽烟")

class Mother:
    def __init__(self, age):
        self.age = age
    def cook(self):
        print("会做饭")

# 子类
class Son(Father, Mother):
    def __init__(self, name, age, sex):

        # 显式调用：不推荐
        # Father.__init__(self, name)
        # Mother.__init__(self, age)

        # 隐式调用：推荐
        # 注意继承顺序：先继承儿子类的超类父亲类，再继承父类后面的母亲类
        # super(class , self).__init__(attribute)  # 默认的参数调用
        super().__init__(name)  # 即 super(Son, self).__init__(name)
        super(Father, self).__init__(age)

        self.sex = sex

    def play_game(self):
            print("会打游戏")

son = Son("小明",20,'男')
print(son.name, son.age, son.sex)
son.smoke()
son.cook()
son.play_game()


# 继承链
print(Son.__mro__)
# (<class '__main__.Son'>,
# <class '__main__.Father'>,
# <class '__main__.Mother'>,
# <class 'object'>)