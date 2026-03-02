
# 1. print输出,打印内容, 在控制台输出内容
print("hello")
print('%')
print("hello", "world!",999)

print("---------------------------------------------------------------")

# sep=" " 分隔符,默认是空格, 打印多个内容时的连接符号
# sep是Separator的缩写，意为 “分离, 分开, 分隔, 分居, 隔, 隔开”
# 可以查看Python函数源码: ctrl + 鼠标左键
print("sep分隔符默认使用空格分隔参数", 666)
print("sep可更改默认空格为任意字符串", 666, sep="*")

print("---------------------------------------------------------------")

# end="\n" 结束符,默认是\n表示换行符
#     \n : 表示换行
#     \t : 表示制表符
print("end结束符默认换行")
print(666)
print("end可更改换行符为制表符", end="\t")
print(666)
print("end也可输出字符串代替结束符",  end="$$$")
print(666)

print("---------------------------------------------------------------")

# 练习: 打印以下内容,使用sep将唱,跳,rap连接
#     "唱+跳+rap"
print(end='\t')
print('"',end='')
print("唱","跳","rap",sep='+',end='')  # 输出为	"唱+跳+rap"
print('"')

print("---------------------------------------------------------------")

# 2.输入: input()
#  方便我们测试代码时自定义输入值
# Python中比较常见的3种类型: int整数, float小数, str字符串 "hello"

# 特点:
#    1.会让程序暂停,等待用户输入内容,且按enter键
#    2.input会得到一个str字符串类型,如果输入的是数字,则需要使用int或float来转换
# 快速添加或取消注释: ctrl + /

name = input("文字提示，请输入姓名：")
print("用户输入名字为：",name)
# age = input("input your age: ")
# print(age + 5)   # 此用法错误
# print(type(age))   # type用于检索数据类型 <class 'str'>
# print(type(int(age)))   # int()强制类型转换为整数类型  <class 'int'>
# print(type(float(age)))   # int()强制类型转换为整数类型  <class 'float'>
# print(int(age) + 5)   # 28
age = int(input("input your age: "))
print(age + 5)   # 28


# 示例:
#    输入1个数,然后将这个数 乘以 3.14
num = float(input("请输入一个数字: "))
print(num * 3.14)



# 练习:
# 1、输入1个名字, 用一个变量接收该名字，然后输出该变量的值
# 2、输入任意两个数字,计算他们的和

name = input("请输入一个名字: ")
print(name)
num1 = int(input("input num1: "))
num2 = int(input("input num2: "))
print(num1 + num2)

