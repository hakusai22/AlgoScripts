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
# @Time    : 2024/07/17 16:45
# @题目     :
# @参考     :  
# 时间复杂度 :

import pandas as pd

if __name__ == '__main__':
    # Load the Excel file
    file_path = '/Users/yinpeng/GoWorkSpace/Go_Python_Study/Python3_Basis/excel/daily_verse.xlsx'
    df_daily_verse = pd.read_excel(file_path, sheet_name='daily')

    # Generate SQL update statements
    sql_statements = []
    for _, row in df_daily_verse.iterrows():
        print(row)
        print(row['monthdaycode'], row['Prayer'], row['Reflection'], row['Inspiration'])
        monthdaycode = row['monthdaycode']
        prayer = row['Prayer'].replace("'", "''")  # Escape single quotes
        reflection = row['Reflection'].replace("'", "''")  # Escape single quotes
        inspiration = row['Inspiration'].replace("'", "''")  # Escape single quotes

        sql = f"UPDATE wepray_bible_daily_verse SET prayer='{prayer}', reflection='{reflection}', inspiration='{inspiration}' WHERE monthDayCode={monthdaycode};"
        sql_statements.append(sql)

    # Write the SQL statements to a file
    output_file_path = '/Users/yinpeng/GoWorkSpace/Go_Python_Study/Python3_Basis/excel/update_statements.sql'
    with open(output_file_path, 'w') as file:
        for statement in sql_statements:
            file.write(statement + '\n')
