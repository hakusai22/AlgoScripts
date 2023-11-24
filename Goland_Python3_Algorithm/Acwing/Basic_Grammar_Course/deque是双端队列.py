# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:48
from collections import deque

if __name__ == '__main__':
    a = deque([1, 2, 3])
    a.append(1)
    print(a)
    a.appendleft(3)
    print(a)
    a.popleft()
    print(a)
    a.pop()
    print(a)
