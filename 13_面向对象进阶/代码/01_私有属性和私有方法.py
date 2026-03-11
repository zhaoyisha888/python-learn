
# 私有属性和私有方法  属性名或者方法名下面添加两个下划线
# 公有属性和公有方法


class Girl:
    def __init__(self, name, age, face_value):
        # 公有属性
        self.name = name
        self.age = age
        # 私有属性：
        #   1.只能在当前类内部使用
        #   2.属性名下面要添加两个下划线
        self.__face_value = face_value
    
    # 公有方法
    def work(self):
        if self.age > 22:
            print(f"今年{self.age}岁了，已经参加工作了")
        else:
            print(f"今年才{self.age}岁，不能当童工")

    def have_boyfriend(self):
        self.__sing()  # 当前类内部可以调用
        print(f"颜值{self.__face_value}，很好找对象")

    # 私有方法
    def __sing(self):
        print(f"{self.name}会唱歌")

# 创建对象
girl1 = Girl("lin", 28, 90)
girl2 = Girl("Ann", 12, 100)
print(girl1.name)
print(girl1.age)
# 私有属性不允许在类外部用
# print(girl1.__face_value)  # AttributeError: 'Girl' object has no attribute '__face_value'. Did you mean: '_Girl__face_value'?
# 私有方法不允许在类外部用
# girl2.__sing()    # AttributeError: 'Girl' object has no attribute '__sing'

# 类的内部可以调用（间接使用）
girl2.have_boyfriend()  
'''
Ann会唱歌
颜值100，很好找对象
'''

# 扩展:不建议使用（暂时不确定是否能正常使用）
# 特殊:可以通过内部属性调用  _类名__私有属性
# print(girl1._Girl.__face_value)
# girl2._Girl.__sing()