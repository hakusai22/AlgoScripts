# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:53

if __name__ == '__main__':
    li = [[1, 3], [8, 10], [2, 6], [15, 18]]
    li.sort(key=lambda x: x[0])
    print(li)
