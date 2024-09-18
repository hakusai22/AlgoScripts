import json
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

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
# @Time    : 2024/09/10 09:49
# @题目     :
# @参考     :  
# 时间复杂度 :

if __name__ == '__main__':
    # We will now split the 'audio_content' column into 'introduction' and 'Final thoughts' columns
    # based on the delimiter "<break time=\"2000ms\" />"
    # 读取Excel文件
    file_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/wepray/wepray_session.xlsx'
    df = pd.read_excel(file_path,sheet_name="Sheet1")
    split_columns = df['audio_content'].str.split('<break time="2000ms" />', expand=True, n=1)
    df['introduction'] = json.dumps(split_columns[0])  # First part before the break
    df['Final thoughts'] = json.dumps(split_columns[1].str.strip())
    df_cleaned = df.drop(columns=['audio_content'])

    # Save the cleaned DataFrame to a new Excel file
    output_path = '/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/excel/wepray/output_file333.xlsx'  # Update with the desired output file path
    df_cleaned.to_excel(output_path, index=False)

