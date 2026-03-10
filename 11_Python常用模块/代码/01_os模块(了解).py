import os

# os  用于获取系统的功能，主要用于操作文件或者文件夹

print(os.name)  # nt 表示window操作系统
print(os.getcwd())  # 当前目录

# 创建目录: mkdir()  如果文件存在会报错
# 创建多层目录: makedirs('a/b/c')

os.mkdir('a')  # 当前目录下创建a目录
if not os.path.exists('a'):
    os.mkdir('a')

os.makedirs('a/b/c')  # 当前目录下创建a/b/c目录


# 删除空目录: rmdir
os.rmdir('a')


# 删除文件: remove
os.remove('b.txt')


# 重命名: rename
os.rename('a.txt', 'b.txt')



# listdir() : 返回指定目录下的所有文件或文件夹名组成的列表
# dir_list = os.listdir('D:\\code\\python-learn\\11_Python常用模块\\代码')
dir_list = os.listdir(r'D:\code\python-learn') # 路径前用r'表示原始字符串，路径中的\不需要转义了
print(dir_list)

# os.path
#  os.path.exists : 文件或文件夹是否存在
#  os.path.isfile() : 是否为文件
# os.path.isdir() : 是否为目录
print(os.path.exists('D:\\code\\python-learn')) # True
print(os.path.isfile('D:\\code\\python-learn')) # False 文件夹不是单个文件
print(os.path.isdir('D:\\code\\python-learn')) # True 文件夹是目录



# 合并路径
print(os.path.join('D:\\code\\python-learn', 'a.py'))   # 不用纠结是否存在
# D:\code\python-learn\a.py



# 需求: 将指定目录下的子目录的绝对路径打印
path = r'D:\code\python-learn\11_Python常用模块\代码'
dir_list = os.listdir(path)  # 获取指定目录下的 所有文件或文件夹名, 组成列表
print(dir_list)   # 结果是一个列表，不是绝对路径

for dir_name in dir_list:   # 遍历列表进行拼接得到各个文件或文件夹的绝对路径
    dir_path = os.path.join(path, dir_name)
    # print(dir_path)

    if os.path.isdir(dir_path):  # 判断是否为目录
        print("文件：", dir_path)
    else:
        print("目录：", dir_path)

'''
目录： D:\code\python-learn\11_Python常用模块\代码\01_os模块(了解).py
目录： D:\code\python-learn\11_Python常用模块\代码\02_json模块.py
目录： D:\code\python-learn\11_Python常用模块\代码\03_时间模块time和datetime.py
目录： D:\code\python-learn\11_Python常用模块\代码\04_文件操作.py
文件： D:\code\python-learn\11_Python常用模块\代码\10作业答案
目录： D:\code\python-learn\11_Python常用模块\代码\hello.json
目录： D:\code\python-learn\11_Python常用模块\代码\hello.xml
'''


# 绝对路径: 从盘符开始的路径
# 相对路径: 从当前文件所在目录开始的路径

# os.path.split : 拆分 (了解)
print(os.path.split(r'D:\code\python-learn\11_Python常用模块\代码\02_json模块.py'))
# ('D:\\code\\python-learn\\11_Python常用模块\\代码', '02_json模块.py') 结果是一个元组，从尾部拆开

# os.path.splitext() : 拆分文件的扩展名
print(os.path.splitext(r'02_json模块.py'))
# ('02_json模块', '.py') 结果是一个元组，从尾部拆开，文件名和扩展名分开

# 文件大小:字节 (了解)
print(os.path.getsize(r'hello.json'))  # 204 注意参数只能是文件名，不能是路径

# 获取某个文件或者文件夹的绝对路径 (了解)
print(os.path.abspath('hello.json'))  # D:\code\python-learn\11_Python常用模块\代码\hello.json

# 对比绝对路径，os.getcwd()可以获取当前工作目录
print(os.getcwd())  # D:\code\python-learn\11_Python常用模块\代码


