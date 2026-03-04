
# 列表的功能：对列表中元素操作
#    增删改查

# 1. 增加: 添加元素
#    append(n) : 在列表的末尾追加元素
#    insert(i, n) : 在下标i的位置插入元素n，原来的元素后移
#    extend(iterable) : 在列表末尾添加多个元素
#           iterable:列表/元组/字符串/字典/集合
# 注意append和extend区别
nums = [1, 2, 3]

nums.append(1)
print(nums, len(nums))

nums.insert(0, 4)
print(nums,len(nums))

nums.extend([9, 6])
print(nums, len(nums))

# 区分append和extend
nums.append([1, 2, 3])
print(nums, len(nums))

nums.extend('abc')   # 不建议这样写
print(nums, len(nums))
# append只增加1个元素，extend增加多个元素



# 2. 删除:
#    pop(i) : 弹出(删除并返回)下标i对应的元素, 默认删除最后一个元素
#    remove(n) : 删除指定元素n，一次只能删除1个元素
#    clear() : 清空列表
nums = [1, 2, 3, 4, 5, 6]
print(nums.pop(), nums)  # 6
print(nums.pop(3), nums) # 4

nums = [1, 2, 3, 3, 5, 6]
nums.remove(3)   # 删除指定元素3
print(nums)


# count(): 计数,统计列表中元素出现的次数
nums = [1, 2, 3, 3, 5, 6]
# 删除列表中所有3
while nums.count(3):  
    nums.remove(3)
print(nums)

# clear() : 了解，列表还在，只是清空了列表中的元素
nums.clear()
print(nums)




# 3. 改: 修改元素，利用索引
nums = [1, 2, 3, 4, 5, 6]
nums[1] = 9
print(nums)

# 4. 查: 查询
#  索引: nums[1]
#  切片: nums[2:4]
#  循环: for n in nums:
#        for i in range():
#        for i,n in enumerate(nums):


# index(n) : 获取元素n第一次出现的下标,如果元素不存在则报错（了解）
nums = [1, 2, 3, 3, 3, 6]
print(nums.index(3))  # 2
print(nums.index(3, 1))  # 2 从下标1开始查找元素3
# print(nums.index(5))  # ValueError: 5 is not in list


# 排序
#   sort() : 默认升序排列, 直接修改原列表
##     sorted(): 默认升序排列, 不改变原列表 (了解)
#   reverse() : 倒序,逆序, 直接修改原列表
##     reversed() : 倒序,逆序, 不改变原列表 (了解)
nums = [1, 2, 4, 4, 8, 5, 5, 6]

nums.sort()  
print(nums)   # [1, 2, 4, 4, 5, 5, 6, 8]
nums.sort(reverse=True)  # 降序
print(nums)   # [8, 6, 5, 5, 4, 4, 2, 1]

nums = [1, 2, 4, 4, 8, 5, 5, 6]
nums.reverse()  
print(nums)   # [6, 5, 5, 8, 4, 4, 2, 1]

# sorted() : 排序, 不改变原列表
nums = [1, 2, 4, 4, 88, 5, 5, 6]
nums2 = sorted(nums)
print(nums, nums2)    # [1, 2, 4, 4, 88, 5, 5, 6] [1, 2, 4, 4, 5, 5, 6, 88]

# reversed() : 倒叙, 不改变原列表
nums = [1, 4, 88, 5, 5, 6]
nums2 = reversed(nums)
print(nums[::-1])    # 倒叙，不修改原列表 [6, 5, 5, 88, 4, 1]
print(nums, nums2, list(nums2))   # [1, 4, 88, 5, 5, 6] <list_reverseiterator object at 0x000001FD0B46FFD0> [6, 5, 5, 88, 4, 1]




# copy(): 复制,拷贝
nums = [1,2,3]
nums2 = nums
print(nums, nums2)   # [1, 2, 3] [1, 2, 3]
nums2[0] = 666
print(nums, nums2)   # [666, 2, 3] [666, 2, 3]

nums2 = nums.copy()
nums2[0] = 999
print(nums, nums2)



