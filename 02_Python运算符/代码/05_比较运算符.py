
# 比较运算符/关系运算符/条件运算符
#  > >=(大于或者等于) < <= == !=
#  得到的结果一定是bool类型
print(1 > 2)  # False
print(1 >= 2)  # False
print(1 < 2)  # True
print(1 <= 2)  # True

print(True == 1)   # True
print(False == 0, end='\n\n')   # True
 
# 字符串和字符串比较
# 比较规则：从左往右依次一个一个字符比较，如果能比较出大小则直接返回结果
#  ASCII码：
#  a~z : 97~122
#  A~Z : 65~90
#  0~9 : 48~57
print('A' > 'a')
print('abcdf' > 'abe')    # 顺序比较，第一个不同的字符比较大小，后面的字符不再比较
# print('0' > 1)  # TypeError: '>' not supported between instances of 'str' and 'int'

n = 5
print(10> n > 1)  # True,python支持这种写法, 相当于 10>n and n>1,其他语言不支持这种写法



# 练习：
# 7. BMI（身体质量指数）的计算公式为 BMI=体重（千克）/身高的平方（米）
#   请输入您的身高 和 体重，计算BMI值，判断是否在18.5~25之间？

print ("请输入您的身高和体重，计算BMI值，判断是否在18.5~25之间？")
higght = float(input('请输入身高（单位m）：'))
weight = float(input('请输入体重，单位kg）：'))
BMI = weight / (higght ** 2)
result = 18.5 <= BMI <= 25   # 等价于 18.5 <= BMI and BMI <= 25
if result: 
    result = '在18.5~25之间'
else:
    result = '不在18.5~25之间'
print(f"您的BMI值为{BMI:.2f},{result}")

