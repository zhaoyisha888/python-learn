''' '''
# 练习：
# 1. 打印1-100之间的所有偶数
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

# 2.求 1-100之间可以被6整除的数的个数
total = 0
num = 1
while num <= 100:
    if num %6 ==0:
        total += 1
    num += 1
print(total)

# 3. 打印1-100之间的所有奇数
num = 1
while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1

# 4.计算1到100以内所有偶数的和。
sum = 0
num = 1
while num <= 100:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)

# 5.计算1到100以内所有能被3或者7整除的数的和。
sum = 0
num = 1
while num <= 100:
    if num % 3 == 0 or num % 7 == 0:
        sum += num
    num += 1
print(sum)

# 6.计算1到100以内能同时被7和3整除的数的个数。
total = 0
num = 1
while num <= 100:
    if num % 3 == 0 and num % 7 == 0:
        total += 1
    num += 1
print(total)

