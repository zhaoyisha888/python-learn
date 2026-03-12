
# 1. 利用封装和继承的特性完成如下操作：
# 小学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打架
#
# 中学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 谈恋爱
#
# 大学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打游戏

class Student():
    def __init__(self, name, number, age, sex):
        self.name = name
        self.number = number
        self.age = age
        self.gender = sex

    def study(self):
        print("学习中...")

# 子类完全继承父的的属性，可以不用super()初始化，直接调用父类初始化属性

class PrimaryStudent(Student):
    def __init__(self, name, number, age, sex):
        super(PrimaryStudent, self).__init__(name, number, age, sex)

    # 重写学习方法
    def study(self):
        print(f"小学生{self.name}学习的内容为：语文 数学 英语")

    def fight(self):
        print("打架中...")

        
class MiddleStudent(Student):
    def __init__(self, name, number, age, sex):
        super(MiddleStudent, self).__init__(name, number, age, sex)

    # 重写学习方法
    def study(self):
        print(f"中学生{self.name}学习的内容为：语数外 生物化 史地政")

    def talk(self):
        print("谈恋爱中...")
        

class CollegeStudent(Student):
    def __init__(self, name, number, age, sex):
        super(CollegeStudent, self).__init__(name, number, age, sex)
    
    # 重写学习方法
    def study(self):
        print(f"大学生{self.name}逃课中..")

    def play(self):
        print(f"{self.name}打游戏中...")




# 调用：
# 创建小学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语文 数学 英语
#
# 创建中学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语数外 生物化 史地政
#
# 创建大学生对象
#    调用学习的方法：
#    打印内容为： xx 逃课中..
stu1 = PrimaryStudent("小王", "201901", 12, "男")
stu1.study()

stu2 = MiddleStudent("张三", "201002", 12, "男")
stu2.study()

stu3 = CollegeStudent("皇甫铁牛", "1919001", 12, "男")
stu3.study()
