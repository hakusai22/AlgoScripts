from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys
import json

import pandas as pd
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
# @Time    : 2024/09/11 10:24
# @题目     :
# @参考     :  
# 时间复杂度 :

if __name__ == '__main__':
    file_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/wepray/intro_end.xlsx'
    df = pd.read_excel(file_path, sheet_name="Sheet1", engine='openpyxl')
    print(df['introduction_content'].replace('\n', '\\n\\n'))
    print(df['final'].replace('\n', '\\n\\n'))
    df['introduction_content'] = df['introduction_content'].replace('\n', '\\n\\n')
    df['final'] = df['final'].replace('\n', '\\n\\n')

    # # df['introduction_content'] = json.dumps(df['introduction_content'][1])  # First part before the break
    # # df['Final thoughts'] = json.dumps(df['Final thoughts'][1])
    #
    # Save the cleaned DataFrame to a new Excel file
    output_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/wepray/output_file1.xlsx'  # Update with the desired output file path
    df.to_excel(output_path, index=False)
