
# 异常处理

# 错误：代码还没运行就已经出错了， 这种情况要先解决
# 异常：代码写的时候不报错，运行报错

# 防止某个模块出错导致所有模块都不执行



# 1. 捕获异常
# 异常处理：针对有一定概率(小概率)出现异常的，我们需要做异常处理
# try-except:
#   尝试执行try中的代码，如果出错则进入except，否则不进入
#   作用是：防止报错导致程序结束，出现的错误可以被except捕获

# 下面这段没运行是没有异常的
# a = 0
# n = 6/a   # ZeroDivisionError: division by zero
# print("出现报错，程序终止执行，我不会被打印")  

try:  # 尝试执行代码
    a = 0
    n = 6/a    
    print("try这里会捕获错误，捕获立即进入except，所以我也不会被打印")
except:
    print("出现报错，程序继续执行")   


print()


# 可以捕获具体是什么异常
try:  
    a = 0
    n = 6/a    
    print("try捕获错误，我不会被打印") 
except Exception as e:   # Exception所有异常类的父类
    print(e, type(e))    # division by zero <class 'ZeroDivisionError'>
    print("出现报错，程序继续执行")   
except IndexError as e:   # 可以根据不同的异常进入不同的except
    print(e)    
    print("出现报错 IndexError") 


print()


# try-except-else
#   try尝试执行代码，如果出错了就进入except,否则进入else
try:  
    a = 3
    n = 6/a    
    print(n) 
except Exception as e:   
    print("error：", e)   
else:  
    print('没问题')    


print()


# try-except-finally
#    try尝试执行代码，如果出错了就进入except, 最终进入finally(不管有没有错)


try:  
    a = 0
    n = 6/a    
    print(n) 
except Exception as e:   
    print("error：", e)   
finally:   
    print('不管有没有错误，这句都会执行')    


print()


# Python自带的异常类型:
#     AttributeError : 属性错误
#     NameError: 变量没定义
#     IndexError : 索引越界
#     ZeroDivisionError : 除以0的错误
#     KeyError : 字典的key错误
#     FileExistsError : 文件已经存在
#     FileNotFoundError : 文件不存在
#     ImportError : 导包错误
#     IndentationError : 缩进错误
#     SyntaxError : 语法错误

# 2. 主动抛出异常（了解）
# 这个语句前后没有错误操作，属于主动创造一个错误，内容可以自己编
raise Exception("主动抛出异常")   # Exception: 主动抛出异常
raise IndexError("索引出错")     # IndexError: 索引出错

# 3. 断言 assert
def fn(n):
    # 断定n != 0，如果判定错误，则抛出异常"n不能为0"
    assert n != 0, "n不能为0"     
    print(5/n)

fn(5)
fn(0)   # AssertionError: n不能为0