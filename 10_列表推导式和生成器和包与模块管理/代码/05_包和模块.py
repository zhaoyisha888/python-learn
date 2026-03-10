''' '''

# 包 package : 是一个有__init__.py文件夹
# 模块 module: 是一个python文件

# 封装思路: 项目 => 包(文件夹) => 模块(python文件) => 类 => 函数 => 代码

# 创建包
# 创建模块

# 导入模块
#   import
#   from - import


# 精确导入

from time import sleep
sleep(1)

# 模糊导入 : * 表示所有内容
from time import *
print(time())

# 自定义模块
# 没有外套一个包
'''
# 模糊导入，导入整个模块
import module
print(module.name)
module.func()
'''

'''
# 精确导入，只导入其中一个或者多个
from module import name,func
print(name)
# print(module.name)   # NameError: name 'module' is not defined
func()
'''

# 模块在包中
'''
from package1 import module1
print(module1.name)
module1.func()
'''

from package1.module1 import name
print(name)

# 别名: as 改名后只能用别名
import module as modu
print(modu.name)
modu.func()

from package1 import module1 as modu1
modu1.func()
