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
# @Time    : 2024/09/26 10:13
# @题目     :
# @参考     :  
# 时间复杂度 :

import numpy as np
import pandas as pd


def loadData():
    items = {'A': {'Alice': 5.0, 'user1': 3.0, 'user2': 4.0, 'user3': 3.0, 'user4': 1.0},
             'B': {'Alice': 3.0, 'user1': 1.0, 'user2': 3.0, 'user3': 3.0, 'user4': 5.0},
             'C': {'Alice': 4.0, 'user1': 2.0, 'user2': 4.0, 'user3': 1.0, 'user4': 5.0},
             'D': {'Alice': 4.0, 'user1': 3.0, 'user2': 3.0, 'user3': 5.0, 'user4': 2.0},
             'E': {'user1': 3.0, 'user2': 5.0, 'user3': 4.0, 'user4': 1.0}
             }
    return items


if __name__ == '__main__':
    item_data = loadData()

    similarity_matrix = pd.DataFrame(
        np.identity(len(item_data)),
        index=item_data.keys(),
        columns=item_data.keys(),
    )

    # 遍历每条物品-用户评分数据
    for i1, users1 in item_data.items():
        for i2, users2 in item_data.items():
            if i1 == i2:
                continue
            vec1, vec2 = [], []
            for user, rating1 in users1.items():
                rating2 = users2.get(user, -1)
                if rating2 == -1:
                    continue
                vec1.append(rating1)
                vec2.append(rating2)
            similarity_matrix[i1][i2] = np.corrcoef(vec1, vec2)[0][1]

    print(similarity_matrix)


    target_user = 'Alice'
    target_item = 'E'
    num = 2

    sim_items = []
    sim_items_list = similarity_matrix[target_item].sort_values(ascending=False).index.tolist()
    for item in sim_items_list:
        # 如果target_user对物品item评分过
        if target_user in item_data[item]:
            sim_items.append(item)
        if len(sim_items) == num:
            break
    print(f'与物品{target_item}最相似的{num}个物品为：{sim_items}')

    target_user_mean_rating = np.mean(list(item_data[target_item].values()))
    weighted_scores = 0.
    corr_values_sum = 0.

    target_item = 'E'
    for item in sim_items:
        corr_value = similarity_matrix[target_item][item]
        user_mean_rating = np.mean(list(item_data[item].values()))

        weighted_scores += corr_value * (item_data[item][target_user] - user_mean_rating)
        corr_values_sum += corr_value

    target_item_pred = target_user_mean_rating + weighted_scores / corr_values_sum
    print(f'用户{target_user}对物品{target_item}的预测评分为：{target_item_pred}')

