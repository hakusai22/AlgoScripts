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
# @Time    : 2024/09/26 10:18
# @题目     :
# @参考     :  
# 时间复杂度 :

from itertools import combinations
import pandas as pd

alpha = 0.5
top_k = 20

def load_data(train_path):
    train_data = pd.read_csv(train_path, sep="\t", engine="python", names=["userid", "itemid", "rate"])  # 提取用户交互记录数据
    print(train_data.head(3))
    return train_data

def get_uitems_iusers(train):
    u_items = dict()
    i_users = dict()
    for index, row in train.iterrows():  # 处理用户交互记录
        u_items.setdefault(row["userid"], set())
        i_users.setdefault(row["itemid"], set())
        u_items[row["userid"]].add(row["itemid"])  # 得到user交互过的所有item
        i_users[row["itemid"]].add(row["userid"])  # 得到item交互过的所有user
    print("使用的用户个数为：{}".format(len(u_items)))
    print("使用的item个数为：{}".format(len(i_users)))
    return u_items, i_users

def swing_model(u_items, i_users):
    # print([i for i in i_users.values()][:5])
    # print([i for i in u_items.values()][:5])
    item_pairs = list(combinations(i_users.keys(), 2))  # 全排列组合对
    print("item pairs length：{}".format(len(item_pairs)))
    item_sim_dict = dict()
    for (i, j) in item_pairs:
        user_pairs = list(combinations(i_users[i] & i_users[j], 2))  # item_i和item_j对应的user取交集后全排列 得到user对
        result = 0
        for (u, v) in user_pairs:
            result += 1 / (alpha + list(u_items[u] & u_items[v]).__len__())  # 分数公式
        if result != 0:
            item_sim_dict.setdefault(i, dict())
            item_sim_dict[i][j] = format(result, '.6f')
    return item_sim_dict

def save_item_sims(item_sim_dict, top_k, path):
    new_item_sim_dict = dict()
    try:
        writer = open(path, 'w', encoding='utf-8')
        for item, sim_items in item_sim_dict.items():
            new_item_sim_dict.setdefault(item, dict())
            new_item_sim_dict[item] = dict(
                sorted(sim_items.items(), key=lambda k: k[1], reverse=True)[:top_k])  # 排序取出 top_k个相似的item
            writer.write('item_id:%d\t%s\n' % (item, new_item_sim_dict[item]))
        print("SUCCESS: top_{} item saved".format(top_k))
    except Exception as e:
        print(e.args)

if __name__ == "__main__":
    train_data_path = "./ratings_final.txt"
    item_sim_save_path = "./item_sim_dict.txt"
    top_k = 10  # 与item相似的前 k 个item
    train = load_data(train_data_path)
    u_items, i_users = get_uitems_iusers(train)
    item_sim_dict = swing_model(u_items, i_users)
    save_item_sims(item_sim_dict, top_k, item_sim_save_path)
