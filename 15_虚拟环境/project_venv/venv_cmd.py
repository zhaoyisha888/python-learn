import requests

"""
(.venv) PS D:\code\python-learn\15_虚拟环境\project_venv> pip freeze
certifi==2026.2.25
charset-normalizer==3.4.5
idna==3.11
requests==2.32.5
urllib3==2.6.3

"""

# 在本项目目录下创建一个新的虚拟环境
# 使用命令 python -m venv .cmd_venv  （.cmd_venv就是虚拟环境的名称）
# windows下使用 .cmd_venv\Scripts\activate 激活指定环境cmd_venv
# 此时终端提示环境路径(.venv)变化为(.cmd_venv)：
"""
(.venv) PS D:\code\python-learn\15_虚拟环境\project_venv> python -m venv .cmd_venv
(.venv) PS D:\code\python-learn\15_虚拟环境\project_venv> .cmd_venv\Scripts\activate
(.cmd_venv) PS D:\code\python-learn\15_虚拟环境\project_venv> 
"""

# 查看这个新建的环境有什么包，如下为空白的虚拟环境
# 可以随意安装自己需要的包，这是与(.venv)环境隔离开的，互相不影响
"""
(.cmd_venv) PS D:\code\python-learn\15_虚拟环境\project_venv> pip freeze
(.cmd_venv) PS D:\code\python-learn\15_虚拟环境\project_venv> pip list
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0

[notice] A new release of pip is available: 24.0 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
"""

# 使用完后要记得退出虚拟环境，使用 deactivate 命令即可
# 终端提示前没有虚拟环境的括号说明正确退出
"""
(.cmd_venv) PS D:\code\python-learn\15_虚拟环境\project_venv> deactivate
PS D:\code\python-learn\15_虚拟环境\project_venv> 
"""


# 删除虚拟环境用 rm -rf .venv  （.venv根据实际环境名称更改）
# 谨慎删除虚拟环境（一般不建议删除）