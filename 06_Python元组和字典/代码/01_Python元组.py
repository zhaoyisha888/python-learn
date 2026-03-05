
# # 元组 tuple
# #    元组就是不可变的列表（不能修改）

# # 元组的基本操作
# # 1. 创建元组
# tuple = (1, )     # 表示1个元素的元组，必须加逗号
# # tuple = (1)
# tuple_none = ()   
# print(tuple, tuple_none, type(tuple), type(tuple_none))


# # 2. 索引 （同列表）
# t = (1, 2, 5)
# print(t[0])   # 1
# print(t[1])   # 2
# print(t[2])   # 5
# print(t[-1])   # 5
# # print(t[3])    # IndexError: tuple index out of range

# # 3. 长度 （同列表）
# print(len(t))


# # 4.遍历（同列表）
# for i in t:       # item in tuple
#     print(i, end="")
# print()

# for i in range(len(t)):         # index in range
#     print(t[i], end="")
# print()

# for i, n in enumerate(t):       # enum : index, item in tuple
#     print(i, n)


# # 5.修改元素 （不可以修改元素）
# # t[0] = 666     # TypeError: 'tuple' object does not support item assignment


# # 6.切片（同列表）
# tuple = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# print(tuple[1:3])
# print(tuple[:6])
# print(tuple[3:8:2])


# # 7.加法 （同列表）
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print(t1 + t2)    # (1, 2, 3, 4, 5, 6)

# # 8.乘法（同列表）  
# print(t1 * 3)     # (1, 2, 3, 1, 2, 3, 1, 2, 3) 重复

# # 9.成员 （同列表）
# if 1 in t1:       # 判断1是否在t1中
#     print("1在t1中")


# # 元组的功能
# # 增 : 不可以
# # 删 : 不可以
# # 改 : 不可以
# # 查 : 索引，切片，循环

# # 只携带两种方法
# # tuple.count()
# # tuple.index()

# # 排序(不修改原元组，返回的是列表)
# tuple = (1, 2, 3, 4, 5, 6)
# tuple_new1 = sorted(tuple)
# tuple_new2 = reversed(tuple)
# print(tuple_new1)           # [1, 2, 3, 4, 5, 6]
# print(tuple_new2, list(tuple_new2))   # <reversed object at 0x000002304913FF70> [6, 5, 4, 3, 2, 1]

# # 转换成list
# nums = list(tuple)
# print(nums)
# # 后面就可以使用list方法了


# # index() : 了解 （同列表）
# print(tuple.index(3))           # 2，注意不要越界


# # count(): 计数，了解 （同列表）
# tuple = (1, 4, 4, 4, 4, 4, 3)
# print(tuple.count(4))           # 5个四



# # 扩展 ：快速取值
# x, y, z = 1, 2, 3
# print(x, y, z)
# x, y, z = [1, 2, 3]
# print(x, y, z)
# x, y, z = (1, 2, 3)
# print(x, y, z)

# x, _ = (1, 2)
# print(x)
# print(_)

t = tuple([1, 2, 3])  # 列表转元组，前面的tuple = (...)覆盖了tuple内置函数，会报错 TypeError: 'tuple' object is not callable
print(t)



