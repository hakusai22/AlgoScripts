# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 22:50

#
# 浅拷贝会创建新对象，其内容非原对象本身的引用，而是原对象内第一层对象的引用。
# 浅拷贝有三种形式:切片操作、工厂函数、copy 模块中的 copy 函数。
# 比如上述的列表 a，切片操作：b = a[:] 或者 b = [x for x in a]；
# 工厂函数：b = list(a)；
# copy 函数：b = copy.copy(a)；
import copy

if __name__ == '__main__':
    a = [1, 2, "hello", ['python', 'C++']]
    b = copy.copy(a)
    c = list(a)
    d = a[:]
    e = [x for x in a]
    print(a is b)
    print(c is a)
    print(d is a)
    print(e is a)
