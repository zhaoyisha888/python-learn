
# from test import sort

# # 同级模块导入不用包名，否则 ModuleNotFoundError: No module named 'test.sort'
# from test.sort import sort1 as sort_max_to_min
# from test.sort import sort2 as sort_min_to_max
# from test.sort import find_index as find_same_index


from sort import sort1 as sort_max_to_min
from sort import sort2 as sort_min_to_max
from sort import find_index as find_same_index

s = [1, 15, 2, 3, 99, 4, 5, 6, 7, 8, 7, 8, 9, 10]

print (f'列表s降序排列为{sort_max_to_min(s)}')

print (f'列表s升序排列为{sort_min_to_max(s)}')

n = int(input('请输入要查找的数字：'))
total = 0
for i in range(len(s)):
    if s[i] == n:
        total += 1
print (f'数字{n}在列表s中出现了{total}次，下标分别为{find_same_index(s, n)}')


'''
列表s降序排列为[99, 15, 10, 9, 8, 8, 7, 7, 6, 5, 4, 3, 2, 1]
列表s升序排列为[1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10, 15, 99]
请输入要查找的数字：7
数字7在列表s中出现了2次，下标分别为[8, 10]
'''