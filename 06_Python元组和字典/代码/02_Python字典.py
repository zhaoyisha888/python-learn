from distutils.command.install import value

# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）, 如果key重复，后面的value会覆盖前面的value
#   2. 字典的key不可以是 可变类型(list,dict,set)，可以是数字，但是建议使用字符串
#   3.  key无序性

# 1.创建
#  key:value ：键值对
d = {"name":"张三","age":18}


# 2.索引 : 没有数字索引，但是可以使用key
print(d["name"])
# print(d[0])   # KeyError: 0
print(d.get("age"), d.get("age2"))   # 18 None   get方法: 如果key不存在，返回None
print(d.get("sex", "男"))    # 男   get(key , default): Return the value for key if key is in the dictionary, else default.

# 3.长度
print(len(d))


# 4.遍历(理想结果是键值对)
print(d.keys())   # dict_keys(['name', 'age'])
print(d.values())  #dict_values(['张三', 18])
print(d.items())   # dict_items([('name', '张三'), ('age', 18)])

for k in d:            
    print(k,d[k])      # 推荐
# for k in d.keys():   
#     print(k)         # 不推荐，只有键
# for v in d.values():   
#     print(v)         # 不推荐， 使用场景比较少，只有值
for k,v in d.items():
    print(k,v)         # 推荐， 键值对


# 5.修改元素
d["name"] = "李四"
print(d)               # {'name': '李四', 'age': 18}


# 6.切片: 不可以
   # dict没有数字索引，是无序的，所以不可以切片


# 7.合并
d1 = {"name": "lucy"}
d2 = {"age": 20}
# print(d1 + d2)     # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

d1.update(d2)    # 将d2合并到d1里
print(d1, d2)    # {'name': 'lucy', 'age': 20} {'age': 20}


# 8.重复： 不可以
# print(d1 * 3)   # TypeError: unsupported operand type(s) for *: 'dict' and 'int'


# 9.成员 (掌握)
d = {'name': 'lucy', 'age': 20}
if 'name' in d:
    print("name is a key of the dict")


# 字典的功能
# 增删改查
#  增，改
d = {'name': 'lucy', 'age': 20}
d['name'] = 'lily'  # 修改
print(d)
d['sex'] = '女'   # sex本来不存在，新增
print(d)         # {'name': 'lily', 'age': 20, 'sex': '女'}


# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）
d = {'name': 'lily', 'age': 20, 'sex': '女'}
d.pop('name')   # 删除name
print(d)   # {'age': 20, 'sex': '女'}

d.clear()
print(d)   # {}   清空字典

d = {'a': 1, 'b': 20,'c': 6}
d.popitem()   # 随机删除一个元素, 一般删除最后一个元素
print(d)   # {'a': 1, 'b': 20}

