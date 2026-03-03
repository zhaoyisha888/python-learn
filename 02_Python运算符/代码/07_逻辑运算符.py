
# 逻辑运算符
#   and与(且)  or或者  not非（取反）

# and: 并且 （有假为假）
#   2边都为True则为True，只要有一个是False 则为False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


# or：或者  (有真为真)
#   2边都为False则为False, 只要有一个是True则为True
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False 


# not 非，取反
print(not True)   # False
print(not False)  # True

# 不同数据类型 隐式bool值 判断 (基本都是空为假，或者0/false/non为假)
#   数字类型： 0是假，其他为真
#   字符串类型： 空字符串''为假，其他为真
#   list类型：空列表[]是假，其他为真
#   tuple元组： 空元组()为假,其他为真
#   dict字典：空字典{}为假，其他为真
#   bool类型： False为假，True为真
#   NoneType类型: None是假
print()
# '''
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(True))
print(bool(None))
# '''
print()




# 扩展: and和or的短路运算

# and: 
#  从左往右依次判断每一个数，只要有一个是False（bool值隐式判断） 则返回该数
# print(True and 6 and 8)          # 8, 全真输出最后一个值

# print(True and 0 and print(9))   # 0, 哪个值使能短路，就输出此值，后面的值不再判断
# print(False and 0 and 6)         # False
# print(0 and False)               # 0

print(print(10) and 5)       # 打印10，然后打印None。print函数返回None，None是假，所以输出None


# or:
#  从左往右依次判断每一个数，只要有一个是True（bool值隐式判断） 则返回该数
print(False or 0)              # 0, 全假输出最后一个值
print(0 or print(90) or 8 or 20)     # 先打印90，然后打印None。8是第一个真，所以最后输出8




# 练习：请直接写出答案（先不要运行）
# x = True and 9                # 9
# y = False or True or 8        # True
# z = x * 3 + y * 2             # 29
# print(x, y, z)            # 9 True 29

# and 保留最后一个真值，or保留第一个真值



