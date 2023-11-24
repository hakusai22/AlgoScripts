
from typing import List, Tuple, Optional
from collections import defaultdict, Counter
from sortedcontainers import SortedList

MOD = int(1e9 + 7)
INF = int(1e20)
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 23:23

if __name__ == '__main__':
    n = eval(input())

    print(n // 365, 'ano(s)')
    print(n % 365 // 30, 'mes(es)')
    print(n % 365 % 30, 'dia(s)')