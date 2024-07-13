# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 16:33
import sys

if __name__ == '__main__':
    # sys.argv是一个列表，是python命令后的各个参数列表，且所有的值都为字符串
    print(sys.argv)
    # python3 py_sys.py 1 2 3asdfa asda
    # ['py_sys.py', '1', '2', '3asdfa', 'asda']

    # 查看Python搜索模块的系统路径，不同操作系统不同
    print(sys.path)
    # / usr / bin / python3 / Users / yinpeng / PythonWorkSpace / Algorithm - study / py标准库 / py_sys.py
    # ['/Users/yinpeng/PythonWorkSpace/Algorithm-study/py标准库/py_sys.py']
    # ['/Users/yinpeng/PythonWorkSpace/Algorithm-study/py标准库', '/Users/yinpeng/PythonWorkSpace/Algorithm-study',
    #  '/Users/yinpeng/PythonWorkSpace/Algorithm-study/leetcode周赛/leetcode周赛/第298场',
    #  '/Users/yinpeng/PythonWorkSpace/Algorithm-study/六月_区间求和', '/Users/yinpeng/PythonWorkSpace/Algorithm-study/src',
    #  '/Users/yinpeng/PythonWorkSpace/Algorithm-study/leetcode周赛',
    #  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
    #  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip',
    #  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8',
    #  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload',
    #  '/Users/yinpeng/Library/Python/3.8/lib/python/site-packages',
    #  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages',
    #  '/Library/Python/3.8/site-packages',
    #  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']

    # 变量sys.platform用来显示当前操作系统的相关信息：
    print(sys.platform)
    # darwin

    # Windows: win32。
    # Mac: darwin。
    # Linux: linux2。
