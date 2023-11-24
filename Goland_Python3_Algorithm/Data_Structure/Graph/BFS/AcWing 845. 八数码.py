from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/06 11:34

"""
    在一个 3×3的网格中，1∼8这 8个数字和一个 x 恰好不重不漏地分布在这 3×3  的网格中。
    1 2 3
    x 4 6
    7 5 8
    在游戏过程中，可以把 x 与其上、下、左、右四个方向之一的数字交换（如果存在）。
    我们的目的是通过交换，使得网格变为如下排列（称为正确排列）：
    1 2 3
    4 5 6
    7 8 x
    输出占一行，包含一个整数，表示最少交换次数
    
    穷举出所有给定序列通过交换能得到的新序列，在穷举过程中保存交换次数。
    在穷举过程中，如果出现了结果序列，就输出交换次数。
    起始状态： 为 1 2 3 x 4 6 7 5 8
    
    交换一次：
        x 与上方元素交换得到： x 2 3 1 4 6 7 5 8
        x 与右方元素交换得到： 1 2 3 4 x 6 7 5 8
        x 与下方元素交换得到： 1 2 3 7 4 6 x 5 8
        
    交换两次得到：
        2 x 3 1 4 6 7 5 8
        1 x 3 4 2 6 7 5 8
        1 2 3 4 6 x 7 5 8
        1 2 3 4 5 6 7 x 8
        1 2 3 7 4 6 5 x 8    
    
    交换三次得到：
        2 3 x 1 4 6 7 5 8
        .....
        1 2 3 4 5 6 7 8 x
    得到了最终结果，输出 3.
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    end = "12345678x"
    # 记录每个状态的交换次数，初始状态为0
    d = {start: 0}
    # 记录队列头结点到了哪个状态
    q = deque([start])
    while len(q):
        # 头结点出队
        t = q.popleft()
        # 保存当前头结点距离初始状态的交换次数
        distance = d[t]
        if t == end:
            return distance

        # 找下表，交换顺序
        idx = t.find('x')
        x = idx // 3
        y = idx % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                # 字符串不能够交换，所以先转成列表再交换
                t = list(t)
                t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]
                t = ''.join(t)
                # 如果新的状态不在字典里
                if t not in d:
                    # 添加新的状态进入字典并且赋值为上一个状态的交换次数 + 1
                    d[t] = distance + 1
                    # 将新的状态入队
                    q.append(t)
                # 记得一定要回退状态
                t = list(t)
                t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]
                t = ''.join(t)

    return -1

n = input().split()
start = ''
for c in n:
    start += c

print(bfs(start))
