
# 集合 set
#   特点: 唯一性(去重), 无序性, 元素不能是可变类型(list,dict,set)

# 1.创建集合
s = {1, 2, 3, 3, 3, 6}
print(s)    # {1, 2, 3, 6}

# s = {1, 2, 3, 3, 3, [1, 2, 3]}     # TypeError: unhashable type: 'list'

s1 = {}  # 空字典,不是空集合
print(s1, type(s1))    # {} <class 'dict'>

s2 = set()  # 空集合
print(s2, type(s2))    # set() <class 'set'>


# 2.不能用索引
# print(s[0])    # TypeError: 'set' object is not subscriptable


# 3.长度
print(len(s))  # 4，去重后的长度

# 4.循环(仅仅一种)
for i in s:
    print(i)


# 5.修改:删除一个,然后再添加新的
# 6.不能用切片
# 7.不能用加法
# 8.不能用乘法
# 9.成员
print('小王' in s)      # False
print(1 in s)           # True


# 功能(了解)
#  add(): 添加元素
#  pop(): 删除元素
#  clear(): 清空
#  remove(3)  # 删除元素3,如果元素不存在会报错
#  discard(3)  # 删除元素3,如果元素不存在不会报错
s = {1, 2, 3, 4}

s.add(5)   # 添加元素5
print(s)   # {1, 2, 3, 4, 5}

s.pop()    # 随机删除一个元素
print(s)

s.clear()
print(s)    # set()

# s.remove(3)   # KeyError: 3   上一步已经清空，现在是空集合，3不存在

s = {1, 2, 3, 4}
s.discard(3)  
s.discard(300)  # 不会报错 
print(s)         # {1, 2, 4}


## 集合关系
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # 且  交集  {3, 4}
print(s1 | s2)  # 或  并集 {1, 2, 3, 4, 5, 6}
print(s1 - s2)  # 差集（相对补集） {1, 2}, 只存在s1中的元素
print(s1 >= s2)  # 包含关系 True ,表示s1中是否全部包含s2的元素


# # 练习：利用集合去重，输出去重后的新列表
nums = [1, 3, 3, 2, 2, 2, 4, 5, 4, 5]
# 空间复杂度 O(n)：占用内存大小
# 时间复杂度 O(n)：运行消耗时间

n = set(nums)  # 元素顺序会变
print(nums, list(n))  # [1, 3, 3, 2, 2, 2, 4, 5, 4, 5] [1, 2, 3, 4, 5]



