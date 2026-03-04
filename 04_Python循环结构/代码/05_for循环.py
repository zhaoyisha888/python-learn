
# 使用场景：
#   while循环： ①无限循环， ②未知循环次数
#   for循环：一般使用在已知循环次数




# 打印1~100的每一个数
'''
i = 1
while i<= 100:
    print(i)
    i += 1
'''

# for-in循环：
#  每次循环，i会自动等于右边range中的每一个数
for i in range(1, 5):
    print(i, sep=" ", end=" ")
print()

# 练习：求1~100的累加和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)



# for循环使用场景
# 1.和range结合
#   比如：循环1~10，找到能被3整除的数
for i in range(1, 11):
    if i % 3 == 0:
        print(i)


# 2.和列表结合
# 列表的基本操作
#  元素：列表中的每一个值
nums = [1, 2, 3, 2]

# 索引：从0开始
print(nums[0])  # 1
print(nums[1])  # 2
print(nums[2])  # 3
print(nums[3])  # 2
# print(nums[4])  # 报错：IndexError: list index out of range
print(nums[-1])  # 2，-1表示倒数第一个元素 

#  列表长度：元素个数：len()
print(len(nums))  # 4


print()


# 循环遍历列表的四种写法
for n in nums:
    print(n)    # 元素

for i in range(4):  # 索引 range(4) => [0,1,2,3]
    print(i, nums[i])  # 索引 元素

for i in range(len(nums)):  # 长度转索引 ，len(nums) = 4 ，range(4) => [0,1,2,3]
    print(i, nums[i])  # 索引 元素

# enumerate：枚举，可以同时得到索引和元素
# 缺点是不如range()灵活，range()可以取部分索引元素，enumerate()只能取全部索引元素
for i,n in enumerate(nums):
    print(i, n)


print()


# 还可以使用for的有：
#    range()
#    list: [1,2,3]
#    dict: {'name': 'ikun', 'age': 20}
#    tuple: (1,2,3)
#    set: {1,2,3}
#    str: "hello"



