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
# @Time    : 2024/09/26 10:56
# @题目     :
# @参考     :  
# 时间复杂度 :

"""
而这次介绍的这个模型是2014年由Facebook提出的GBDT+LR模型， 该模型利用GBDT自动进行特征筛选和组合， 进而生成新的离散特征向量，
 再把该特征向量当做LR模型的输入， 来产生最后的预测结果， 该模型能够综合利用用户、物品和上下文等多种不同的特征， 生成较为全面的推荐结果， 
 在CTR点击率预估场景下使用较为广泛。
 
GBDT全称梯度提升决策树，在传统机器学习算法里面是对真实分布拟合的最好的几种算法之一，
在前几年深度学习还没有大行其道之前，gbdt在各种竞赛是大放异彩。原因大概有几个，
一是效果确实挺不错。二是即可以用于分类也可以用于回归。三是可以筛选特征， 所以这个模型依然是一个非常重要的模型。

GBDT是通过采用加法模型(即基函数的线性组合），以及不断减小训练过程产生的误差来达到将数据分类或者回归的算法

通过GBDT进行特征组合之后得到的离散向量是和训练数据的原特征一块作为逻辑回归的输入， 而不仅仅全是这种离散特征
建树的时候用ensemble建树的原因就是一棵树的表达能力很弱，不足以表达多个有区分性的特征组合，多棵树的表达能力更强一些。GBDT每棵树都在学习前面棵树尚存的不足，迭代多少次就会生成多少棵树。
RF也是多棵树，但从效果上有实践证明不如GBDT。且GBDT前面的树，特征分裂主要体现对多数样本有区分度的特征；后面的树，主要体现的是经过前N颗树，残差仍然较大的少数样本。优先选用在整体上有区分度的特征，再选用针对少数样本有区分度的特征，思路更加合理，这应该也是用GBDT的原因。
在CRT预估中， GBDT一般会建立两类树(非ID特征建一类， ID类特征建一类)， AD，ID类特征在CTR预估中是非常重要的特征，直接将AD，ID作为feature进行建树不可行，故考虑为每个AD，ID建GBDT树。
非ID类树：不以细粒度的ID建树，此类树作为base，即便曝光少的广告、广告主，仍可以通过此类树得到有区分性的特征、特征组合
ID类树：以细粒度 的ID建一类树，用于发现曝光充分的ID对应有区分性的特征、特征组合
"""

import pandas as pd

# gbm = lgb.LGBMRegressor(objective='binary',
#                         subsample=0.8,
#                         min_child_weight=0.5,
#                         colsample_bytree=0.7,
#                         num_leaves=100,
#                         max_depth=12,
#                         learning_rate=0.05,
#                         n_estimators=10,
#                         )
#
# gbm.fit(x_train, y_train,
#         eval_set=[(x_train, y_train), (x_val, y_val)],
#         eval_names=['train', 'val'],
#         eval_metric='binary_logloss',
#         # early_stopping_rounds = 100,
#         )
#
# model = gbm.booster_  # 获取到建立的树
#
# # 每个样本落在每个树的位置 ， 下面两个是矩阵  (样本个数, 树的棵树)  ， 每一个数字代表某个样本落在了某个数的哪个叶子节点
# gbdt_feats_train = model.predict(train, pred_leaf=True)
# gbdt_feats_test = model.predict(test, pred_leaf=True)
#
# # 把上面的矩阵转成新的样本-特征的形式， 与原有的数据集合并
# gbdt_feats_name = ['gbdt_leaf_' + str(i) for i in range(gbdt_feats_train.shape[1])]
# df_train_gbdt_feats = pd.DataFrame(gbdt_feats_train, columns=gbdt_feats_name)
# df_test_gbdt_feats = pd.DataFrame(gbdt_feats_test, columns=gbdt_feats_name)
#
# # 构造新数据集
# train = pd.concat([train, df_train_gbdt_feats], axis=1)
# test = pd.concat([test, df_test_gbdt_feats], axis=1)
# train_len = train.shape[0]
# data = pd.concat([train, test])
#
# # 新数据的新特征进行读入编码
# for col in gbdt_feats_name:
#     onehot_feats = pd.get_dummies(data[col], prefix=col)
#     data.drop([col], axis=1, inplace=True)
#     data = pd.concat([data, onehot_feats], axis=1)
#
# # 划分数据集
# train = data[: train_len]
# test = data[train_len:]
#
# x_train, x_val, y_train, y_val = train_test_split(train, target, test_size=0.3, random_state=2018)
#
# # 新数据的新特征进行读入编码
# for col in gbdt_feats_name:
#     onehot_feats = pd.get_dummies(data[col], prefix=col)
#     data.drop([col], axis=1, inplace=True)
#     data = pd.concat([data, onehot_feats], axis=1)
#
# # 划分数据集
# train = data[: train_len]
# test = data[train_len:]
#
# x_train, x_val, y_train, y_val = train_test_split(train, target, test_size=0.3, random_state=2018)
