
import json

# json: 一种表示数据的格式
# json的2种表现形式:
#    1.json字符串
#    2.json对象(Python字典)

# 注意: json文件不能写注释, 不能有多余的逗号, 只能用双引号表示字符串

# json解析(json反序列化): (重点)
#   字符串 => Python字典  json.loads()

s = '{"name": "张三", "age": 20}'
json.loads(s)  # json字符串 => Python字典
print(type(s), type(json.loads(s)))   # <class 'str'> <class 'dict'>


# json序列化:  (了解)
#    Python字典 => 字符串  json.dumps()

py_dict = {"name": "张三", "age": 20}
json.dumps(py_dict)  # Python字典 => json字符串
print(type(py_dict), type(json.dumps(py_dict)))  # <class 'dict'> <

