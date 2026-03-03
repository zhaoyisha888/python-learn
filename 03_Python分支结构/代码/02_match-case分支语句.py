
# 输入您的等级，输出对应的成绩范围
#    A ：  >= 90
#    B ：70 ~ 90
#    C : 60 ~ 70
#    D :  < 60

# match-case : Python3.10及以上版本
# 了解
# 类似 switch-case  匹配的是一个固定的值，范围判断不太好用

n = input("请输入您的等级（A/B/C/D）：")
match n:
    case 'A':                            # 字符类型，区分大小写，ASCII码值不同，A和a是不同的
        print("成绩范围：>= 90")
    case 'B':
        print("成绩范围：70 ~ 90")
    case 'C':
        print("成绩范围：60 ~ 70")
    case 'D':
        print("成绩范围：< 60")
    # 其他情况
    case _:                        # _ 代表其他情况，相当于default，但是不用专门写break
        print("输入不合法！")               
'''
Python 从设计上就规避了 case 穿透问题，执行完匹配到的分支就直接跳出 match 结构，不用专门写break
    如果没有匹配到，会执行case _: 
    如果没写 case _: 通配分支，且所有 case 都没匹配到，程序静默地跳过整个 match 结构继续执行后续代码，不报错且无输出。

'''

# switch-case穿透：
# 简单来说就是当 case 分支里没有写 break 语句时，程序会继续执行后续 case 分支的代码，而不会跳出 switch 结构
# 直到遇到 break 语句或者 switch 结构结束。