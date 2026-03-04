
# Python数据类型:
#  int, float, str, bool, NoneType,
#  list, tuple, dict, set(了解), bytes

# list列表 : Array数组
# 为什么要使用列表：
# 举例：如果我们表示汽车品牌用变量保存单个值
a = "BYD"
b = "五菱宏光"
c = "小米"
d = "蔚来"
e = "法拉利"
f = "兰博基尼"
g = "路虎"

# 如果要你表示300个品牌, 变量就太多了，这时我们可以使用列表来表示：
cars = ["BYD", "五菱宏光", "小米", "蔚来", "蔚来", "法拉利", "兰博基尼", "路虎"]



# 列表的基本功能
# 1.列表定义
nums = [1, 2, "hello"]  # 列表中可以存放任意类型的数据，但是一般不建议这样做

# 2.索引,下标
#   从0开始
print(nums[0])    # 1
print(nums[1])
print(nums[2])    # hello
# print(nums[3])  # IndexError: list index out of range
print(nums[-1])   # 倒数第一个元素
print(nums[-2])   # 倒数第二个元素

# 3.长度,元素个数
print(len(nums))  # 3

# 4.遍历,循环
nums = [1, 2, "hello"]
for item in nums:          # 直接打印元素
    print(item)

for i in range(len(nums)):  # 通过索引打印元素
    print(nums[i])

for i,n in enumerate(nums):    # 枚举打印索引和元素
    print(i, n)

# 5.修改列表(通过索引直接修改该元素)
nums = [1, 2, "hello"]
nums[0] = 100
print(nums)     # [100, 2, 'hello']

# 6.切片 (很重要) : 不会修改原列表
#    list[start : stop : step] : [start, stop), step步长默认1，负数索引从后往前数
#  和range(start, stop, step)类似  [start, stop)
ages = [18, 19, 20, 21, 22, 23]
print(ages[:])      # 整个列表 -> [18, 19, 20, 21, 22, 23]
print(ages[:3])     # 取索引[0,3} -> [18, 19, 20]
print(ages[3:])     # 取索引[3, 最后) -> [21, 22, 23]
print(ages[::2])    # 取整个列表，步长为2 -> [18, 20, 22]

print(ages[::-1])   # 列表倒序 -> [23, 22, 21, 20, 19, 18]
print(ages[1:3:1])   # 正序切片 -> [19, 20]
print(ages[3:1:-1])  # 倒序切片 -> [21, 20] 
# 倒序切片: 从后往前数，先数到索引为3，再数到索引为1，不包括索引1，然后可以切片
# 不能倒数负数取数，负数索引从-1开始，没有0，-1为最后一个元素，-2为倒数第二个元素，以此类推

# 7. 合并 +  (了解)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)   # [1, 2, 3, 4, 5, 6]

# 8. 重复 * (了解)
print(a * 3)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 9. 成员 in (掌握，一般结合if语句在列表中判断某个元素是否存在)
if 1 in a:  # 判断1是否在列表a中
    print("1在列表a中")

# 需求: 列表去重 (掌握)
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = []
for i in nums1:
    if i not in nums2:   # 判断i是否在nums2中，如果不在，就添加到nums2中
        nums2.append(i)   # append()方法向列表末尾添加元素
print(nums2)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 10.删除元素 del (了解)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del nums[0]         # 删除索引为0的元素
print(nums)         # [20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums[1:5])    # [30, 40, 50, 60]
del nums[1:5]       # 再删除索引为1到3的元素，不包含3
print(nums)         # [20, 70, 80, 90, 100]

