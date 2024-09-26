from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

# @Author  : https://github.com/hakusai22
# @Time    : 2024/09/26 10:52
# @题目     :
# @参考     :  
# 时间复杂度 :


"""
召回早前经历的第一代协同过滤技术，让模型可以在数量级巨大的item集中找到用户潜在想要看到的商品。
这种方式有很明显的缺点，一个是对于用户而言，只能通过他历史行为去构建候选集，并且会基于算力的局限做截断。
所以推荐结果的多样性和新颖性比较局限，导致推荐的有可能都是用户看过的或者买过的商品。
之后在Facebook开源了FASSI库之后，基于内积模型的向量检索方案得到了广泛应用，也就是第二代召回技术。
这种技术通过将用户和物品用向量表示，然后用内积的大小度量兴趣，借助向量索引实现大规模的全量检索。
这里虽然改善了第一代的无法全局检索的缺点，然而这种模式下存在索引构建和模型优化目标不一致的问题，
索引优化是基于向量的近似误差，而召回问题的目标是最大化topK召回率。且这类方法也不方便在用户和物品之间做特征组合。

所以阿里开发了一种可以承载各种深度模型来检索用户潜在兴趣的推荐算法解决方案。
这个TDM模型是基于树结构，利用树结构对全量商品进行检索，将复杂度由O(N)下降到O(logN)。

"""
