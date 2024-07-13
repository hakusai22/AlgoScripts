# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/22 20:05


# 用BFS按层遍历，答案是最后一层的第一个节点的值
# https://leetcode.cn/problems/find-bottom-left-tree-value/
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    queue, ans = Deque([root]), None
    while queue:
        ans = queue[0].val
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
