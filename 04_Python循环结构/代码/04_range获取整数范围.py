
# range(start, stop, step=1): 整数范围
#   start: 起始值, 包含   (默认从0开始)
#   stop: 结束值，不包含  [start, stop)前闭后开，左闭右开
#   step: 步长(默认为1) 
#         步长可以是负数，但是起始值必须大于结束值，否则返回空序列
#   返回值: 返回的是一个不可变的整数序列对象（不是列表，但可以轻松转成列表）。


print(list(range(5)))      # [0, 1, 2, 3, 4]
print(list(range(0, 5)))   # [0, 1, 2, 3, 4]
print(list(range(1, 5)))   # [1, 2, 3, 4]
print(list(range(6, 5)))   # []

# 步长
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]



