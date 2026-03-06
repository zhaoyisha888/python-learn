

# 列表推导式: (掌握)
#    使用for循环用一行来生成列表

# 创建一个列表
print(list(range(1, 11)))

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = []
for i in range(1, 11):  # 创建一个列表
    numbers.append(i)
    

# 列表推导式：用一行代码快速生成新列表
# 语法：[表达式 for 变量 in 可迭代对象]

num_list = [i for i in range(1, 11)]
num_list1 = [i*2 for i in range(1, 11)]
print(num_list)
print(num_list1)

# [表达式 for 变量 in 可迭代对象 if 条件]        
num_list = [i for i in range(1, 11) if i % 2 == 0]     # [2, 4, 6, 8, 10]   条件表达式，可得到偶数列表
print(num_list)

num_list2 = [i for i in range(1, 11) if i % 2 and i % 3 == 0]   # [3, 9]
print(num_list2)

num_list3 = [i for i in range(1, 11) if i % 2 if i % 3 == 0]   # [3, 9]   if嵌套，相当于 if i % 2 and i % 3 == 0
print(num_list3)

num_list4 = [i+j for i in 'ABC' for j in '123']  # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']  相当于两个for循环嵌套
print(num_list4)




# 字典推导式(了解，需要有键值对)
d = {f'name{i}':i for i in range(1, 3)}  # {'name1': 1, 'name2': 2}
print(d)




# 集合推导式(了解，更类似列表)
s = {i for i in range(1, 6)}  
print(s)  # {1, 2, 3, 4, 5}