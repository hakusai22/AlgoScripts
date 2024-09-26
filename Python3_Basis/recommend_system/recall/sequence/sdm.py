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
# @Time    : 2024/09/26 10:48
# @题目     :
# @参考     :  
# 时间复杂度 :

"""
SDM模型(Sequential Deep Matching Model)，是阿里团队在2019年CIKM上的一篇paper。和MIND模型一样，是一种序列召回模型，
研究的依然是如何通过用户的历史行为序列去学习到用户的丰富兴趣。 对于MIND，我们已经知道是基于胶囊网络的动态路由机制，设计了一个动态兴趣提取层，
把用户的行为序列通过路由机制聚类，然后映射成了多个兴趣胶囊，以此来获取到用户的广泛兴趣。而SDM模型，
是先把用户的历史序列根据交互的时间分成了短期和长期两类，然后从短期会话和长期行为中分别采取相应的措施(短期的RNN+多头注意力， 长期的Att Net) 
去学习到用户的短期兴趣和长期行为偏好，并巧妙的设计了一个门控网络==有选择==的将长短期兴趣进行融合，以此得到用户的最终兴趣向量。 
这篇paper中的一些亮点，比如长期偏好的行为表示，多头注意力机制学习多兴趣，长短期兴趣的融合机制等，又给了一些看待问题的新角度，
同时，给出了我们一种利用历史行为序列去捕捉用户动态偏好的新思路。
"""
