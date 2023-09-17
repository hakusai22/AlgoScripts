# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 16:39
import os

if __name__ == '__main__':
    print(os.getcwd())  # 当前工作目录 /Users/yinpeng/PythonWorkSpace/Algorithm-study/py标准库
    print(os.curdir)  # 当前工作目录符号： .
    print(os.listdir(os.curdir))  # 当前目录下得的文件 ['py_os.py', 'py_sys.py']
    print(os.linesep)  # 当前操作系统的换行符：
    print(os.sep)  # 当前操作系统的路径分隔符：
    print(os.pathsep)  # 当前操作系统的环境变量PATH中的分隔符
    print(os.environ)  # 环境变量

    print(os.path.isfile("/python3语法基础/py标准库"))  # 检测路径是否为文件。
    print(os.path.isdir("/"))  # 检测路径是否为文件夹。
    print(os.path.exists("/python3语法基础/py标准库"))  # 检测路径是否存在。
    print(os.path.isabs("/python3语法基础/py标准库"))  # 检测路径是否为绝对路径。

    print(os.path.join("test", "a.txt"))  # 使用系统分隔符，将各个部分合并为一个路径
