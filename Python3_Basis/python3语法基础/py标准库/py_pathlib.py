# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 18:10
import pathlib

if __name__ == '__main__':
    # Python 3提供了一个新的模块pathlib，提供了Path类型来进行更方便的路径操作：
    p = pathlib.Path('')

    print(p)
    # 获得当前目录下所有的文件：
    print(list(p.iterdir()))

    print(list(p.glob('*.py')))
    print(p / "abc" / "123.txt")
