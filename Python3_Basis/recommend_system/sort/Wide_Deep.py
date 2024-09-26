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
# @Time    : 2024/09/26 11:08
# @题目     :
# @参考     :  
# 时间复杂度 :

"""
在CTR预估任务中利用手工构造的交叉组合特征来使线性模型具有“记忆性”，使模型记住共现频率较高的特征组合，往往也能达到一个不错的baseline，且可解释性强。但这种方式有着较为明显的缺点：

特征工程需要耗费太多精力。
模型是强行记住这些组合特征的，对于未曾出现过的特征组合，权重系数为0，无法进行泛化。
为了加强模型的泛化能力，研究者引入了DNN结构，将高维稀疏特征编码为低维稠密的Embedding vector，这种基于Embedding的方式能够有效提高模型的泛化能力。但是，基于Embedding的方式可能因为数据长尾分布，导致长尾的一些特征值无法被充分学习，其对应的Embedding vector是不准确的，这便会造成模型泛化过度。

Wide&Deep模型就是围绕记忆性和泛化性进行讨论的，模型能够从历史数据中学习到高频共现的特征组合的能力，称为是模型的Memorization。能够利用特征之间的传递性去探索历史数据中从未出现过的特征组合，称为是模型的Generalization。Wide&Deep兼顾Memorization与Generalization并在Google Play store的场景中成功落地
"""