# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:50
from queue import PriorityQueue

if __name__ == '__main__':
    Q = PriorityQueue()
    Q.put(2)
    Q.put(3)
    Q.put(1)
    Q.put(64756)
    print(Q.get())
