
# 成员运算符（掌握）
#   in,  not in
#   作用：判断某个元素是否在某个序列中

print(3 in [1, 2, 3, 4, 5])  # True  3在a中，返回True
print(3 not in [1, 2, 3, 4, 5])  # False  3在a中，返回False

print('')

# 身份运算符（了解）
#   is,  is not
#   作用：比较内存地址
a = 1
b = 2
print(a is b)  # False  内存地址不同
print(a is not b) # True

# id(): 查看内存地址
print(id(a))   # 140705630876456
print(id(b))   # 140705630876488


# 区别： ==， is区别
#  == 比较的是值是否相等
#  is 比较的是内存地址

