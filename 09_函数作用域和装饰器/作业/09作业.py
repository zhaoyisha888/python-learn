

# 1、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5
'''
import random



# 提示:
#   通过参数数量判断不同的情况
#   1.有1个参数, 嵌套函数
#   2.有2个参数, 返回和
def my_sum(*args):
    if len(args) > 1:
        return sum(args)

    def inner(x):
        # args = (2,)
        return x + args[0]
    return inner

print(my_sum(2,3))
print(my_sum(2)(3))

# 2、封装函数，传入不定数量的数值型参数，返回所有数字的乘积,
# 提示: *args
def number(*args):
    num = 1
    for i in args:
        num *= i
    return num

print(number(1, 2, 5 ,9 ,7))


# 3、 封装一个函数random_color，该函数的返回值为随机十六进制颜色。 RGB
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000000， #0033CC
# 提示: colors = '0123456789ABCDEF'
#      使用random模块
def random_color():
    colors = '0123456789ABCDEF'
    s = '#'
    for i in range(6):
        s += random.choice(colors)
    return s

print(random_color())


# 4、 封装函数，
# 第一个函数create_persons()，
#   创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#      其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#      其中age的值：10-100之间的随机整数 random.randint()
#      其中faceValue的值：0-100之间的随机整数
#
# 第二个函数 get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数 sort_face_value(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons() -> list:
    persons = []
    name_list = ["张三", "李四", "王五", "赵六", "钱七"]
    for i in range(5):
        name = name_list[i]
        age = random.randint(10,100)
        face_value = random.randint(0, 100)
        person = {"name":name,"age":age, "face_value":face_value}
        persons.append(person)

    for person in persons:
        print(person)

    return persons



def get_old(persons):
    # 先找出最大的年龄
    max_age = max(persons, key = lambda d: d["age"])['age']
    print(f'max_age is :{max_age}')
    # 根据最大的年龄，打印多人信息
    for person in persons:
        if person["age"] == max_age:
            print(person)



def sort_face_value(persons):
    persons.sort(key = lambda person: person['face_value'])
    # 逐个打印排序后的person
    for person in persons:
        print(person)


# 调用
persons = create_persons()
# create_persons() # 返回值为列表，并且函数内部直接打印，
print('*'*100)
get_old(persons)
print('*'*100)
sort_face_value(persons)
'''
{'name': '张三', 'age': 14, 'face_value': 21}
{'name': '李四', 'age': 14, 'face_value': 97}
{'name': '王五', 'age': 15, 'face_value': 37}
{'name': '赵六', 'age': 11, 'face_value': 14}
{'name': '钱七', 'age': 15, 'face_value': 12}
****************************************************************************************************
max_age is :15
{'name': '王五', 'age': 15, 'face_value': 37}
{'name': '钱七', 'age': 15, 'face_value': 12}
****************************************************************************************************
{'name': '钱七', 'age': 15, 'face_value': 12}
{'name': '赵六', 'age': 11, 'face_value': 14}
{'name': '张三', 'age': 14, 'face_value': 21}
{'name': '王五', 'age': 15, 'face_value': 37}
{'name': '李四', 'age': 14, 'face_value': 97}
'''


# 6. 给下面的set_age函数添加一个装饰器，
#    要求：在传入age之前判断age不能小于0，如果小于0则传入0，并打印"提示，年龄不能小于0"
def outer(func):
    def inner(args):
        if args < 0:
            print("提示，年龄不能小于0")
            args = 0

        func(args)

    return inner

@outer
def set_age(age):
    print(f'大家好！我今年{age}岁')

set_age(-12)

