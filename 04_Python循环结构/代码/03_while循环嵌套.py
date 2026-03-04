''' '''
# 打印下面的图形，要求一次只能打印一个"*"，写循环嵌套
# 3行5列
'''
*****
*****
*****
'''
raw = 1
while raw <= 3:
    col = 1
    while col <= 5:
        print("*", end="")
        col += 1
    print()
    raw += 1


# 打印下面图形，要求一次只能打印一个"*"
'''
*
**
***
****
*****
'''
raw = 1
while raw <= 5:
    col = 1
    while col <= raw:
        print("*", end="")
        col += 1
    print()
    raw += 1




# 打印一个等腰三角形, 要求一次只能打印一个"*"
'''          i   空格数量     *的数量
    *        1     4(=5-i)     1(=2*i-1)
   ***       2     3           3
  *****      3     2           5 
 *******     4     1           7
*********    5     0           9
'''
raw = 1
while raw <= 5:
    # 同一行
    # 空格
    col = 1
    while col <= 5 - raw:
        print(" ", end = '')
        col += 1
    # *
    col = 1
    while col <= 2 * raw - 1:
        print("*", end = '')
        col += 1
    # 换行输出下一行
    print( )
    raw += 1




