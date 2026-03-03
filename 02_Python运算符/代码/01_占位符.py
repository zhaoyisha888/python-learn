
# f-string (重点掌握)
name = "zys"
age = 23
salary = 1.4567

print('大家好，我是zys，我今年23，我的年薪1.4567亿')
print(f'Hello everyone, my name is {name}, I am {age} years old, my salary is {salary} billion' )



# 占位符：（建议掌握）
#   %s : 字符串
#   %d : 整数
#   %f : 小数   %.4f表示保留4位小数，四舍五入
# print('大家好，我是%s，我今年23，我的年薪1.4567亿' % name)
# print('大家好，我是%s，我今年%d，我的年薪%f亿' %(name, age, salary))
# print('大家好，我是%s，我今年%d，我的年薪%.4f亿' %(name, age, salary))
##   %% : 百分号
print('大家好，我是zys，我今年23%，我的年薪1.4567亿')          # 此处%无语义，只是被当成字符串输出了
# print('大家好，我是%s，我今年23%，我的年薪1.4567亿' % name)    # 此处%有语义 TypeError: not enough arguments for format string
print('大家好，我是%s，我今年23%%，我的年薪1.4567亿' % name)



# 花括号占位符.format() （了解）
print('Hello everyone, my name is {}, I am {} years old, my salary is {} billion'.format(name, age, salary) )
print('Hello everyone, my name is {a}, I am {b} years old, my salary is {c} billion'.format(b = age, c = salary,a = name) )



# 练习：
# 请输入您的姓名，年龄，身高，体重，其中姓名是字符串，年龄是整数，身高和体重是小数类型，
# 要求分别使用上面3种占位符方式输出内容：
#    "大家好，我是xxx, 今年xxx岁，我身高是xx.xcm，体重是xx.xkg"
#
#  例如："大家好，我是Jack, 今年25岁，我身高是177.5cm，体重是75.2kg"

name = input("姓名:")
age = int(input("年龄:"))
height = float(input('身高：'))
weight = float(input('体重：'))
print(f"大家好，我是{name}, 今年{age}岁，我身高是{height:.2f}cm，体重是{weight:.2f}kg")
print('大家好，我是%s, 今年%d岁，我身高是%.2fcm，体重是%.2fkg' % (name, age, height, weight))
print('大家好，我是{}, 今年{}岁，我身高是{:.2f}cm，体重是{:.2f}kg'.format(name, age, height, weight))




# %%
