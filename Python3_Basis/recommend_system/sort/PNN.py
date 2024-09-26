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
# @Time    : 2024/09/26 11:05
# @题目     :
# @参考     :  
# 时间复杂度 :

"""
在特征交叉的相关模型中FM, FFM都证明了特征交叉的重要性，FNN将神经网络的高阶隐式交叉加到了FM的二阶特征交叉上，
一定程度上说明了DNN做特征交叉的有效性。但是对于DNN这种“add”操作的特征交叉并不能充分挖掘类别特征的交叉效果。
PNN虽然也用了DNN来对特征进行交叉组合，但是并不是直接将低阶特征放入DNN中，
而是设计了Product层先对低阶特征进行充分的交叉组合之后再送入到DNN中去。

PNN模型其实是对IPNN和OPNN的总称，两者分别对应的是不同的Product实现方法，前者采用的是inner product，
后者采用的是outer product。在PNN的算法方面，比较重要的部分就是Product Layer的简化实现方法，
需要在数学和代码上都能够比较深入的理解。
"""

# def PNN(dnn_feature_columns, inner=True, outer=True):
#     # 构建输入层，即所有特征对应的Input()层，这里使用字典的形式返回，方便后续构建模型
#     _, sparse_input_dict = build_input_layers(dnn_feature_columns)
#
#     # 构建模型的输入层，模型的输入层不能是字典的形式，应该将字典的形式转换成列表的形式
#     # 注意：这里实际的输入与Input()层的对应，是通过模型输入时候的字典数据的key与对应name的Input层
#     input_layers = list(sparse_input_dict.values())
#
#     # 构建维度为k的embedding层，这里使用字典的形式返回，方便后面搭建模型
#     embedding_layer_dict = build_embedding_layers(dnn_feature_columns, sparse_input_dict, is_linear=False)
#
#     sparse_embed_list = concat_embedding_list(dnn_feature_columns, sparse_input_dict, embedding_layer_dict, flatten=False)
#
#     dnn_inputs = ProductLayer(units=32, use_inner=True, use_outer=True)(sparse_embed_list)
#
#     # 输入到dnn中，需要提前定义需要几个残差块
#     output_layer = get_dnn_logits(dnn_inputs)
#
#     model = Model(input_layers, output_layer)
#     return model
