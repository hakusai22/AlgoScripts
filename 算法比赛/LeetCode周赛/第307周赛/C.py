# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/23 08:37
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}

        def dfs(node, pa):
            if node is None: return
            if node.val == start:
                self.start = node  # 找到感染节点并把它赋值为全局变量
            parents[node] = pa  # 每个节点对应的父节点
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        ans = -1
        vis = {self.start, None}
        q = [self.start]  # 感染开始

        while q:  # 走完为空
            ans += 1
            tmp = q  # 双队列思想
            q = []
            for node in tmp:
                for x in node.left, node.right, parents[node]:
                    if x not in vis:
                        vis.add(x)
                        q.append(x)
        return ans
