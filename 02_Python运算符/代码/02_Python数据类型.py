
# 数据类型：
#   int, float【数字类型：整型int，浮点型[小数]float，复数类型complex 】， 如： 100,  3.14
# 	str【字符串】， 如："hello",  '张三'
# 	bool【布尔类型】：  True真（1）， Flase假（0）
# 	NoneType【空值】 : None
#
# 	list【列表】 类似c语言的数组array， 如： [1, 2, 3]
# 	tuple【元组】 不可改变的列表,  如： (1, 2, 3)
# 	dict【字典】由键值对组成的，如： {"name": "张三",  "age": 30}
# 	set【集合】(了解) ，如： {1, 2, 3}
# 	bytes【字节】二进制， 如：b'hello'

# int 整数
a = 10
print(type(a))    # <class 'int'>

# float: 小数
a =3.14
print(type(a))   # <class 'float'>

# str: 字符串 string
a = 'hello'
print(type(a))    # <class 'str'>

# bool: 布尔类型, True(1), False(0)
a ,b = True, False
# print(type(a,b))   # TypeError: type() takes 1 or 3 arguments
print(a, type(a), type(int (a)), type(b))  # True <class 'bool'> <class 'int'> <class 'bool'>

# NoneType: 空, None (不能与其他类型进行运算)
a = None
print(a, type(a))    # None <class 'NoneType'>
# print(type(int(a)))   # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

# list：列表，数组
a = [1, 2, 3, 3, 3]
print(a, type(a))    # [1, 2, 3] <class 'list'>

# tuple： 元组，不可变的列表
a = (1, 2, 3, 3, 3)
print(a, type(a))    # (1, 2, 3) <class 'tuple'>

# dict: 字典，dictionary (可存放不同类型)
#     key: value  : 键值对
a = {"name": "张三", "age": 20}
print(a, type(a))    # {'name': '张三', 'age': 20} <class 'dict'>
# 访问字典中的值：  字典名[key]
print(a["name"])     
# 修改字典中的值：  字典名[key] = value
a["age"] = 21
print(a["age"])


# set: 集合（了解），内容唯一，重复值会自动去掉
a = {1, 2, 3}
print(a, type(a))    # {1, 2, 3} <class 'set'>
# 集合中的元素是唯一的，不能重复
a = {1, 2, 3, 1, 2, 3}
print(a, type(a))    # {1, 2, 3} <class 'set'>

# bytes: 字节类型，二进制类型 (爬虫爬回的数据一般为二进制数据，需要进行解码)
a = b'hello'
print(a, type(a))    # b'hello' <class 'bytes'>


