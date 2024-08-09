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
# @Time    : 2024/08/06 17:31
# @题目     :
# @参考     :  
# 时间复杂度 :

import pandas as pd

if __name__ == '__main__':
    # 读取Excel文件
    file_path = '/Users/yinpeng/GoWorkSpace/Go_Python_Study/Python3_Basis/excel/google.xlsx'
    df = pd.read_excel(file_path)
    # 去除 originalTransactionId 和 priceInUSD 都重复的行
    df_unique = df.drop_duplicates(subset=['originalTransactionId', 'priceInUSD'])
    # 将去重后的数据保存到一个新的Excel文件
    output_path = '/Users/yinpeng/GoWorkSpace/Go_Python_Study/Python3_Basis/excel/google_output.xlsx'
    df_unique.to_excel(output_path, index=False)

    print(f"去重后的文件已保存到: {output_path}")

