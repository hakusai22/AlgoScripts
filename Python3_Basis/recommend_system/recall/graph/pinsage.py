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
# @Time    : 2024/09/26 10:26
# @题目     :
# @参考     :  
# 时间复杂度 :

# def train(dataset, args):
#     #从dataset中加载数据和原图
#     g = dataset['train-graph']
#     ...
#
#     device = torch.device(args.device)
#     # 为节点随机初始化一个id，用于做embedding
#     g.nodes[user_ntype].data['id'] = torch.arange(g.number_of_nodes(user_ntype))
#     g.nodes[item_ntype].data['id'] = torch.arange(g.number_of_nodes(item_ntype))
#
#
#     # 负责采样出batch_size大小的节点列表: heads, tails,  neg_tails
#     batch_sampler = sampler_module.ItemToItemBatchSampler(
#         g, user_ntype, item_ntype, args.batch_size)
#
#     # 由一个batch中的heads,tails,neg_tails构建训练这个batch所需要的
#     # pos_graph,neg_graph 和 blocks
#     neighbor_sampler = sampler_module.NeighborSampler(
#         g, user_ntype, item_ntype, args.random_walk_length,
#         args.random_walk_restart_prob, args.num_random_walks, args.num_neighbors,
#         args.num_layers)
#
#     # 每次next()返回: pos_graph,neg_graph和blocks，做训练之用
#     collator = sampler_module.PinSAGECollator(neighbor_sampler, g, item_ntype, textset)
#     dataloader = DataLoader(
#         batch_sampler,
#         collate_fn=collator.collate_train,
#         num_workers=args.num_workers)
#
#     # 每次next()返回blocks，做训练中测试之用
#     dataloader_test = DataLoader(
#         torch.arange(g.number_of_nodes(item_ntype)),
#         batch_size=args.batch_size,
#         collate_fn=collator.collate_test,
#         num_workers=args.num_workers)
#     dataloader_it = iter(dataloader)
#
#     # 准备模型
#     model = PinSAGEModel(g, item_ntype, textset, args.hidden_dims, args.num_layers).to(device)
#     opt = torch.optim.Adam(model.parameters(), lr=args.lr)
#
#     # 训练过程
#     for epoch_id in range(args.num_epochs):
#         model.train()
#         for batch_id in tqdm.trange(args.batches_per_epoch):
#             pos_graph, neg_graph, blocks = next(dataloader_it)
#             for i in range(len(blocks)):
#                 blocks[i] = blocks[i].to(device)
#             pos_graph = pos_graph.to(device)
#             neg_graph = neg_graph.to(device)
#
#             loss = model(pos_graph, neg_graph, blocks).mean()
#             opt.zero_grad()
#             loss.backward()
#             opt.step()
