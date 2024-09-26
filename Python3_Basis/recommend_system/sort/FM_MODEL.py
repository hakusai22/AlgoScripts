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
FM模型其实是一种思路，具体的应用稍少。一般来说做推荐CTR预估时最简单的思路就是将特征做线性组合（逻辑回归LR），传入sigmoid中得到一个概率值，本质上这就是一个线性模型，因为sigmoid是单调增函数不会改变里面的线性模型的CTR预测顺序，因此逻辑回归模型效果会比较差。也就是LR的缺点有：
是一个线性模型
每个特征对最终输出结果独立，需要手动特征交叉（xi∗xjxi∗xj），比较麻烦
"""

# class FM(Layer):
#     """显示特征交叉，直接按照优化后的公式实现即可
#     注意：
#         1. 传入进来的参数看起来是一个Embedding权重，没有像公式中出现的特征，那是因
#         为，输入的id特征本质上都是onehot编码，取出对应的embedding就等价于特征乘以
#         权重。所以后续的操作直接就是对特征进行操作
#         2. 在实现过程中，对于公式中的平方的和与和的平方两部分，需要留意是在哪个维度
#         上计算，这样就可以轻松实现FM特征交叉模块
#     """
#
#     def __init__(self, **kwargs):
#         super(FM, self).__init__(**kwargs)
#
#     def build(self, input_shape):
#         if not isinstance(input_shape, list) or len(input_shape) < 2:
#             raise ValueError('`FM` layer should be called \
#                 on a list of at least 2 inputs')
#         super(FM, self).build(input_shape)  # Be sure to call this somewhere!
#
#     def call(self, inputs, **kwargs):
#         """
#         inputs: 是一个列表，列表中每个元素的维度为：(None, 1, emb_dim)， 列表长度
#             为field_num
#         """
#         concated_embeds_value = Concatenate(axis=1)(inputs)  # (None,field_num,emb_dim)
#         # 根据最终优化的公式计算即可，需要注意的是计算过程中是沿着哪个维度计算的，将代码和公式结合起来看会更清晰
#         square_of_sum = tf.square(tf.reduce_sum(
#             concated_embeds_value, axis=1, keepdims=True))  # (None, 1, emb_dim)
#         sum_of_square = tf.reduce_sum(
#             concated_embeds_value * concated_embeds_value,
#             axis=1, keepdims=True)  # (None, 1, emb_dim)
#         cross_term = square_of_sum - sum_of_square
#         cross_term = 0.5 * tf.reduce_sum(cross_term, axis=2, keepdims=False)  # (None,1)
#         return cross_term
#
#     def compute_output_shape(self, input_shape):
#         return (None, 1)
#
#     def get_config(self):
#         return super().get_config()
