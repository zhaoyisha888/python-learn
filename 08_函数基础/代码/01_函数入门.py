''''''
# 封装思路:
#    项目 => 文件夹(包) => 文件(模块) => 类 => 函数 => 代码

'''
问题: 代码重复
     后期维护成本太高
	 代码可读性不高

解决问题：函数
	在一个完整的项目中，某些功能会被反复使用，那么将这部分功能对应的代码提取出来，
	当需要使用功能的时候直接使用
	
本质：对一些特殊功能的封装

优点：
	a.简化代码结构，提高应用的效率
	b.提高代码复用性
	c.提高代码的可读性和可维护性

建议：但凡涉及到功能，都尽量使用函数实现
'''


# 函数定义 : def
def func():
	print("i am a function")

# 函数必须调用才会执行(重复调用)
func()
func()
func()

# 一.函数的参数(必须要掌握)
#  形参: 形式参数，如a,b
#  实参: 实际参数，如5，6
def func1(a, b):    # 形参
	print(f'a + b = {a + b}')

func1(1, 2)         # 实参


# 细分参数种类:
#  1. 必需的位置参数,a, b
#  2. 默认参数, c=7
#  3. 关键字参数, 一般和默认参数结合,有关键字可以打乱顺序 d=88, c=77
def func1(a, b, c=7, d=8):    # 形参
	print(f'a + b = {a + b}, c = {c}, d = {d}')
func1(1, 2)      # a + b = 3, c = 7, d = 8
func1(1, 2, d=88, c=77)    # a + b = 3, c = 77, d = 88



# 4. 不定长参数
# args: argument 参数
# kwargs: keyword argument 关键字参数
#  *args: 接收任意多个位置参数, 元组
#  **kwargs: 接收任意多个关键字参数, 字典


def func2(a):
	print(a)
func2(4)
# func2(4,5)   # TypeError: func2() takes 1 positional argument but 2 were given

def func_many_args(*args, **kwargs):
	print(args, kwargs)

func_many_args(4)   # return a tuple and a blank dict, like (4,) {}
func_many_args(1,2,3, c=77, d=88)   # (1, 2, 3) {'c': 77, 'd': 88}

# 二.返回值: return
#  1. return要写在函数内部, 返回值
#  2. 如果不写return则默认会返回None
#  3. return会立刻结束函数,并返回值
def func3(a, b):
	s = a + b
	# return   # single return, function will end here, and return None
	return s
    # print("i'm behind the return, i will not be executed")

n = func3(1, 2)
print(n)   


# 函数参数顺序(按照位置一一对应)
#   形参顺序: 位置参数，*args,  默认参数，**kwargs
#   实参顺序: 位置参数，        关键字参数
'''
like the function : print()
def print(self, *args, sep=' ', end='\n', file=None):
	pass
the *args usually be used like : print(5, 6)  # 5, 6
arguments like sep=' ' and end='\n' is the **kwargs, include the keyword and the value
'''
def func4(a, *args, **kwargs):
    print(a, args, kwargs)

func4(2, 3, 4, 5, name='xiaoming', age=18)  # 1 2 (3, 4, 5) {'name': 'xiaoming', 'age': 18}

# 通用参数



