
# 练习
# 1.求1-100之间可以被6整除的数的个数
total = 0
for i in range(1,101):
    if i % 6 == 0:
        total += 1
print(total, end="\n\n")

# 2.计算1到100以内所有偶数的和。
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum, end="\n\n")
# 优化
# sum = 0
# for i in range(1,101,2):
#     sum += i
# print(sum, end="\n\n")


# 3.计算1到100以内所有能被3或者7整除的数的和。
sum = 0
for i in range(1,101):
    if i % 3 == 0 or i % 7 == 0:
        sum += i
print(sum, end="\n\n")

# 4.计算1到100以内能同时被7和3整除的数的个数。
total = 0
for i in range(1,101):
    if i % 3 == 0 and i % 7 == 0:
        total += 1
print(total, end="\n\n")

# 5. 求 1-2 + 3-4 + 5-6 ……… + 97-98 + 99-100的结果
sum = 0
for i in range(1,101,2):
    sum += i - (i+1)
print(sum, end="\n\n")   

# 扩展题目：
# 6. 求 1/1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 ……… + 1/97 - 1/98 + 1/99 - 1/100的结果
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum -= 1/i
    else:
        sum += 1/i
print(sum, end="\n\n") 

# 7.丈母娘要彩礼:
#   小伙马上要准备结婚，丈母娘看小伙实诚，同意让小伙分30期给彩礼，分期规则如下
#   分期： 第1天给1分钱     1     2**0
#         第2天给2分钱      2      2**1
#         第3天给4分钱      4       2**2
#         第4天给8分钱      8       2**3    
#         第5天给16分钱    16       2**4
#         ...
#         第30天                   2**29
# 如果是你，会同意吗,为什么？
sum = 0
for i in range(1,31):
    sum += 2**(i-1)
print(sum, end="\n\n") 
# 优化
# sum = 0
# for i in range(30):
#     sum += 2**i
# print(sum, end="\n\n") 