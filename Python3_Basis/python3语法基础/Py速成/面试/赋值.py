# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 22:46

# 在 Python 中，对象的赋值就是简单的对象引用

if __name__ == '__main__':
    a = [1, 2, "hello", ['python', 'C++']]
    b = a
    print(b is a)
