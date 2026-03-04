''' '''

# 循环结构：
#    while循环
#    for-in循环

# 不断做类似的事情，可以使用循环
# 例如，循环打印20次100
n = 1
while n <= 5:
    print(100)
    n += 1

# 循环三要素：循环起始值，循环条件，循环步长



# 死循环：无限循环，循环不会停止
# while True:
#     print("hello")

#  死循环一般可以和input或time.sleep(程序暂停几秒钟)结合使用
# 需求：不断输入年龄，判断该年龄是否大于30
'''
while True:
    age = int(input("请输入年龄："))
    if age > 30:
        print("恭喜你，可以入伍")
        break
    else:
        print("请重新输入")
'''


# 使用场景：
#  1. 无限循环
#  2. 可以是已知循环次数，也可以是未知循环次数

# 需求： 1+2+3+..+100
s = 0
i = 1
while i <= 100:
    # print(i)
    s += i
    i += 1
print(s)      # 5050






# 练习：计算 10 的阶乘 : 1 * 2 * 3 * ...* 10
#   n的阶乘： 1*2*3*..*n
result_num = 1
n = 1
while n <= 10:
    result_num *= n
    n += 1
print(result_num)




# 练习2：求1~100之间的能被6整数的数的和
sum = 0
i = 1
while i <= 100:
    if i % 6 == 0:
        sum += i
    i += 1
print(sum)



# 练习3：求1~100之间的奇数的个数
total = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        total += 1
    i += 1
print(total)



