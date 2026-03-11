
# 1. 自定义模块:
#   a.建立一个包：test
#   b.在包的下创建一个排序的模块 sort.py
#        模块下的功能
#        对列表进行降序排序(不修改原列表) :
#            def sort1(l) -> list:
#
#        对列表进行升序排序(不修改原列表):
#            def sort2(l) -> list:
#
#        获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
#             def find_index(l, n) -> list:
#
#   c.在另外一个文件中 aa.py导入上述包中的模块sort.py，完成模块中功能的调用
from test import sort  # __name__: test.sort


# 2. 开房查询
# 	创建函数，传入一个名字，查找到这哥们的开房记录，
#       然后把身份证号码和地址取出来，写入到以这哥们名字为名的txt文件中 如：张三.txt

def fn(name):
    with open(name + '.txt', 'w', encoding='utf-8') as fp:
        with open('kaifanglist.txt', 'r', encoding='utf-8') as file:  # 只读方式打开开房记录文件
            list_person = file.readlines()
            # print(list_person) # 读取所有行，返回一个列表
            for person in list_person:
                # print(person)  #
                # 使用split()对每行字符串以,进行分割, 返回单人信息列表, 取对应元素的索引
                massages_list = person.split(',')
                if name == massages_list[0]:
                    print(massages_list[1])
                    print(massages_list[4])
                    fp.write("身份证号码：" + massages_list[1] + '\n',)
                    fp.write("地址：" + massages_list[4] + '\n')

input_name = input('请输入要查询的姓名：')
fn(input_name)

# 先思考：
# 最后目的是生成张三.txt文件并往里写信息，所以应该是追加写模式打开文件张三.txt
# 然后只读模式打开原始数据文件kaifanglist.txt，按行处理文件信息并查找姓名
# 向生成文件张三.txt写查到的信息，再关闭只读文件kaifanglist.txt
# 写完信息，关闭生成文件张三.txt
