''''''
# 7. 打印以下图形：
'''
*****
*****
*****
*****
*****
*****
'''
for i in range(6):
    for j in range(5):
        print('*', end='')
    print()




# 8. 打印以下图形：
'''
*
**
***
****
*****
******
'''
for i in range(6):
    for j in range(i+1):
        print('*', end='')
    print()



# 打印图形
'''
1
12
123
1234
12345
123456
'''
for i in range(6):
    for j in range(i+1):
        print(j+1, end='')
    print()



#

# 6. 打印99乘法表
'''
1*1=1
1*2=2  2*2=4
1*3=3  2*3=6  3*3=9

...

1*9=9  2*9=18 3*9=27  ...   9*9=81
'''
# \n : 换行符
# \t : 制表符 tab
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}', end='\t')
    print()



# 练习: for打印下面的等腰三角形
# 打印一个等腰三角形, 要求一次只能打印一个"*"
'''           i   空格数量     *的数量
     *        1     5(=6-i)     1(=2*i-1)
    ***       2     4           3
   *****      3     3           5 
  *******     4     2           7
 *********    5     1           9
***********   6     0           11
'''
for i in range(1,7):    # 1，2，3，4，5，6
    for j in range(6-i):
        print(" ", end = '')
    for j in range(2*i-1):
        print("*", end = '')
    print()
# 7轮打印（错误），0轮次打印5+1个空格， range(2*0-1) ->  range(-1) 起始默认值0>结束值-1，打印结果为一个空格
# for i in range(7):
#     for j in range(6-i):
#         print(" ", end = '')
#     for j in range(2*i-1):
#         print("*", end = '')
#     print()


