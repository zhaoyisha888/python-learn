from tkinter.font import names


# 利用面向对象的思想写下面的程序：直接赋值

# 1.小明穿着白色的特步运动鞋在奥林匹克公园跑步
#   Person类
#      属性：name
#      方法：run(self, place, shoes)
class Person:
    # name = '小明'

    def __init__(self, name):
        self.name = name
        # self.place = place
        # self.shoes = shoes
        # pass                      # 不传参可以不写这个构造方法，或者直接pass
        
    def run(self, place, shoes):
        print(f"{self.name}穿着白色的{shoes}在{place}公园跑步")

p = Person("小明")
p.run("奥林匹克", "特步运动鞋")

print()

# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
#   Person2类
#      属性：name, pig
#      方法：find_pig(self)
class Person2:
    # name = '王梅'
    # pig = '【笨笨】'
    # def __init__(self):
    #     pass                      # 不传参可以不写这个构造方法，或者直接pass

    def __init__(self, name, pig):
        self.name = name
        self.pig = pig
    def find_pig(self):
        print(f"{self.name}家的荷兰宠物猪{self.pig}跑丢了，她哭着贴寻猪启示。")

p = Person2('王梅', '【笨笨】')
p.find_pig()

print()

# 3. 定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆类Circle:
#     属性: 半径r,圆心(Point对象)
#     方法: 周长,面积
#
# 点类Point:
#   属性: x,y
#   方法: 与圆的关系(在圆内/在圆外/在圆上)
import math

class Circle:
    def __init__(self, r, point):
        self.r = r
        self.point = point

    def C(self):
        print('周长:', 2 * math.pi * self.r)

    def S(self):
        print('面积:', math.pi * self.r ** 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def relation(self, circle):
        distance = (self.x - circle.point.x) ** 2 + (self.y - circle.point.y) ** 2
        if distance == circle.r ** 2:
            print(f"点({self.x},{self.y})在圆上")
        elif distance < circle.r ** 2:
            print(f"点({self.x},{self.y})在圆内")
        else:
            print(f"点({self.x},{self.y})在圆外")

circle = Circle(5, Point(0, 0))
circle.C()
circle.S()

point = Point(3, 4)
point.relation(circle)


print()

# 4. 使用面向对象的思想，创建下面的类，对象
#
#  有一个银行账户类 Account,
#     属性包括: 名字name , 余额balance属性
#    方法有：存钱 save_money(self,money)、
#           取钱 get_money(self,money)、
#           查询余额 show_balance(self)。
#    要求：取钱时，要判断余额是否充足，余额不够的时候要提示余额不足
class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def save_money(self,money):
        self.balance += money
        print(f"本次存入{money}，当前余额：{self.balance}")

    def get_money(self,money):
        self.balance -= money
        if self.balance < 0:
            print(f'余额不足')
        else:
            print(f"本次取出{money}，当前余额：{self.balance}")
            

    def show_balance(self):
        print(f"当前余额：{self.balance}")

acc = Account("zhangsan",20000000)
acc.show_balance()
acc.save_money(200000)
acc.get_money(200)

