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
# @Time    : 2024/09/26 10:04
# @题目     :
# @参考     :  
# 时间复杂度 :

"""
协同过滤（Collaborative Filtering）推荐算法是最经典、最常用的推荐算法。基本思想是：
    根据用户之前的喜好以及其他兴趣相近的用户的选择来给用户推荐物品。

目前应用比较广泛的协同过滤算法是基于邻域的方法，主要有：
    基于用户的协同过滤算法（UserCF）：给用户推荐和他兴趣相似的其他用户喜欢的产品。
    基于物品的协同过滤算法（ItemCF）：给用户推荐和他之前喜欢的物品相似的物品。
    不管是 UserCF 还是 ItemCF 算法， 重点是计算用户之间（或物品之间）的相似度。

User-based算法存在两个重大问题：

1. 数据稀疏性
 - 一个大型的电子商务推荐系统一般有非常多的物品，用户可能买的其中不到1%的物品，不同用户之间买的物品重叠性较低，导致算法无法找到一个用户的邻居，即偏好相似的用户。
 - 这导致UserCF不适用于那些正反馈获取较困难的应用场景(如酒店预订， 大件物品购买等低频应用)。
2. 算法扩展性
 - 基于用户的协同过滤需要维护用户相似度矩阵以便快速的找出TopN 相似用户， 该矩阵的存储开销非常大，存储空间随着用户数量的增加而增加。
 - 故不适合用户数据量大的情况使用。
由于UserCF技术上的两点缺陷， 导致很多电商平台并没有采用这种算法， 而是采用了ItemCF算法实现最初的推荐系统。
"""

import numpy as np
import pandas as pd

def loadData():
    users = {'Alice': {'A': 5, 'B': 3, 'C': 4, 'D': 4},
             'user1': {'A': 3, 'B': 1, 'C': 2, 'D': 3, 'E': 3},
             'user2': {'A': 4, 'B': 3, 'C': 4, 'D': 3, 'E': 5},
             'user3': {'A': 3, 'B': 3, 'C': 1, 'D': 5, 'E': 4},
             'user4': {'A': 1, 'B': 5, 'C': 5, 'D': 2, 'E': 1}
             }
    return users

if __name__ == '__main__':
    user_data = loadData()
    similarity_matrix = pd.DataFrame(
        np.identity(len(user_data)),
        index=user_data.keys(),
        columns=user_data.keys(),
    )

    # 遍历每条用户-物品评分数据
    for u1, items1 in user_data.items():
        for u2, items2 in user_data.items():
            if u1 == u2:
                continue
            vec1, vec2 = [], []
            for item, rating1 in items1.items():
                rating2 = items2.get(item, -1)
                if rating2 == -1:
                    continue
                vec1.append(rating1)
                vec2.append(rating2)
            # 计算不同用户之间的皮尔逊相关系数
            similarity_matrix[u1][u2] = np.corrcoef(vec1, vec2)[0][1]

    print(similarity_matrix)

    target_user = 'Alice'
    num = 2
    # 由于最相似的用户为自己，去除本身
    sim_users = similarity_matrix[target_user].sort_values(ascending=False)[1:num+1].index.tolist()
    print(f'与用户{target_user}最相似的{num}个用户为：{sim_users}')

    weighted_scores = 0.
    corr_values_sum = 0.

    target_item = 'E'
    # 基于皮尔逊相关系数预测用户评分
    for user in sim_users:
        corr_value = similarity_matrix[target_user][user]
        user_mean_rating = np.mean(list(user_data[user].values()))

        weighted_scores += corr_value * (user_data[user][target_item] - user_mean_rating)
        corr_values_sum += corr_value

    target_user_mean_rating = np.mean(list(user_data[target_user].values()))
    target_item_pred = target_user_mean_rating + weighted_scores / corr_values_sum
    print(f'用户{target_user}对物品{target_item}的预测评分为：{target_item_pred}')

