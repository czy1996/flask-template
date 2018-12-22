import sys

import app

from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.create_app()
