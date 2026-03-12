# 刚创建项目，先运行终端查看环境包
"""
(.venv) PS D:\code\python-learn\15_虚拟环境\test_venv> pip freeze
(.venv) PS D:\code\python-learn\15_虚拟环境\test_venv>
"""
# 可以看到是一个非常干净的环境
# project_venv里面的虚拟环境的包在这里是不存在的


# 可以根据项目需要导入不同的包，比如flask包
# 再次查看环境里的包，与project_venv里的包不同，互相隔离
import flask
"""
(.venv) PS D:\code\python-learn\15_虚拟环境\test_venv> pip freeze
blinker==1.9.0
click==8.3.1
colorama==0.4.6
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
Werkzeug==3.1.6
"""

# 如果想在本项目里使用project_venv的虚拟环境
# 可以为本项目添加解释器，要找到对应的解释器路径
# 尝试切换，运行报错切换的project_venv环境没有flask包
"""
D:\code\python-learn\15_虚拟环境\project_venv\.venv\Scripts\python.exe D:\code\python-learn\15_虚拟环境\test_venv\test_venv.py 
Traceback (most recent call last):
  File "D:\code\python-learn\15_虚拟环境\test_venv\test_venv.py", line 12, in <module>
    import flask
ModuleNotFoundError: No module named 'flask'
"""

# 环境的迁移
# 使用命令 pip freeze > requeirments.txt 将现有的包导出到 requeirments.txt 文件
# 这里我们把 requeirments.txt 文件迁移到 project_venv 项目中
# 在 project_venv 项目中的终端输入  pip install -r requeirments.txt 命令
"""
(.venv) PS D:\code\python-learn\15_虚拟环境\project_venv> pip install -r requeirments.txt
Collecting blinker==1.9.0 (from -r requeirments.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click==8.3.1 (from -r requeirments.txt (line 2))
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting colorama==0.4.6 (from -r requeirments.txt (line 3))
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached flask-3.1.3-py3-none-any.whl (103 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.3-cp311-cp311-win_amd64.whl (15 kB)
Using cached werkzeug-3.1.6-py3-none-any.whl (225 kB)
Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, Flask
Successfully installed Flask-3.1.3 Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.6 blinker-1.9.0 click-8.3.1 colorama-0.4.6 itsdangerous-2.2.0

[notice] A new release of pip is available: 25.0.1 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip
"""

# 此时再查看该环境中的包，不仅包含原来的包requests，还有requeirments.txt文件里的flask包
"""
(.venv) PS D:\code\python-learn\15_虚拟环境\project_venv> pip freeze
blinker==1.9.0
certifi==2026.2.25
charset-normalizer==3.4.5
click==8.3.1
colorama==0.4.6
Flask==3.1.3
idna==3.11
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
requests==2.32.5
urllib3==2.6.3
Werkzeug==3.1.6
"""
