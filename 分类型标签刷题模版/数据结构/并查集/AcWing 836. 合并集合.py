from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os


"""
    一共有 n个数，编号是 1∼n，最开始每个数各自在一个集合中。
    现在要进行 m个操作，操作共有两种：
        M a b，将编号为 a 和 b的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
        Q a b，询问编号为 a 和 b的两个数是否在同一个集合中；
        
    对于每个询问指令 Q a b，都要输出一个结果，如果 a 和 b 在同一集合内，则输出 Yes，否则输出 No
    数据范围
        1≤n,m≤10^5
"""


if __name__ == '__main__':
    N = 100010
    p = [0] * N

    # find函数，用于返回x的祖宗节点
    # 同时压缩往回搜寻节点的路径
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    n, m = map(int, input().split())

    # 初始化每一个集合，将其集合名字命名为自己的名字
    for i in range(1, n + 1):
        p[i] = i

    # 循环遍历所有输入并进行合并和查询操作
    while m:
        row = list(input().split())
        if row[0] == 'M':
            # 合并的时候将a的根节点插到b的根节点上
            p[find(int(row[1]))] = find(int(row[2]))
        else:
            if find(int(row[1])) == find(int(row[2])):
                print('Yes')
            else:
                print('No')
        m -= 1

