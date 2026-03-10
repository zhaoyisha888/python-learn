
# 迭代器Iterator,
# 可迭代对象Iterable
from collections.abc import Iterator, Iterable

# type(): 查看数据类型
# isinstance() : 判断某个变量是否为某个数据类型
print(3,type(3))    # 3 <class 'int'>
print(isinstance(3, int))  # True 判断3是否为int类型
print(isinstance("hello", (int,float,list)))  # False 判断"hello"是否为int或float或list类型


# 迭代器Iterator (了解)
#    1. 可以使用for循环遍历
#    2. 可以使用next调用

print(isinstance(3, Iterator))  # False
print(isinstance(3.14, Iterator))  # False
print(isinstance("hello", Iterator))  # False
print(isinstance(None, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance([1,2], Iterator))  # False
print(isinstance((1,2), Iterator))  # False
print(isinstance({1:2}, Iterator))  # False
print(isinstance({1,2}, Iterator))  # False
print(isinstance((i for i in range(3)), Iterator))  # True
print()

# 可迭代对象 Iterable
#   1. 可以使用for循环遍历

print(isinstance(3, Iterable))  # False
print(isinstance(3.14, Iterable))  # False
print(isinstance("hello", Iterable))  # True
print(isinstance(None, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance([1,2], Iterable))  # True
print(isinstance((1,2), Iterable))  # True
print(isinstance({1:2}, Iterable))  # True
print(isinstance({1,2}, Iterable))  # True
print(isinstance((i for i in range(3)), Iterable))  # True

print()

# iter() : 可迭代对象 => 迭代器 (了解)
l = [1,2,3]
l2 = iter(l)
print(l,type(l))   # [1, 2, 3] <class 'list'>
print(l2,type(l2))  # <list_iterator object at 0x000001DE8689FB20> <class 'list_iterator'>  
print(next(l2))  # 1  
print(next(l2))  # 2
print(next(l2))  # 3

list(l2)  # 还原迭代器
print(list(l2))  # [] 迭代器已经被next拿完了，剩下的就是空列表了