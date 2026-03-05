
# 1.已知字符串 s = "aAsmr3idd4bgs7Dlsf9eAF",要求如下:

# a.请将s字符串的大写改为小写，小写改为大写: swapcase()
s = "aAsmr3idd4bgs7Dlsf9eAF"
print(s.swapcase())

# b.请将s字符串的数字取出，并输出成一个新的字符串: 循环，isdigit()
s2 = ""
for i in s:
    if i.isdigit():
        s2 += i       # 字符串可加减
print(s2)


# c.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母）, (难度：****)
#    并输出成一个字典。 例 d = {'a':2,'s':1, 'm':1}
#    提示：创建新字典d,循环判断s中字符是否在字典中，在则次数+1
s = "aAsmr3idd4bgs7Dlsf9eAF"
d = {}
for i in s:
    if i.isalpha():
        i = i.lower()  # 将大写字母转换为小写字母
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)


# d.在c题的基础上，输出s字符串出现频率最高的字母, 如果有多个最高,将每个都输出: max(d.values()),再循环
for k,v in d.items():
    if v == max(d.values()):
        print(k, end=" ")
print()


# 2.处理字符串:
#   有字符串 "01#张三#60-02#李四#90-03#王五#70",
#   每一部分表示:  学号#姓名#分数，提取学生信息存放于列表中:
# 结果显示为:
#   [
#     {"学号":'02', '姓名':'李四', '分数':90},
#     {"学号":'03', '姓名':'王五', '分数':70},
#     {"学号":'01', '姓名':'张三', '分数':60}
#   ]
#
# data = "01#张三#60-02#李四#90-03#王五#70"

s = "01#张三#60-02#李四#90-03#王五#70"
list1 = s.split('-')   
print(list1)    # ['01#张三#60', '02#李四#90', '03#王五#70']

stu_list = []
for s in list1:
    list2 = s.split('#')
    stu_dict = {"学号":list2[0], "姓名":list2[1], "分数":list2[2]}
    stu_list.append(stu_dict)
    
print(stu_list)    