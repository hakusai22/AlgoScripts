# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/24 09:01

# Definition for a binary tree node.
from math import inf
from typing import Deque, Optional, List

# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/submissions/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue, ans = Deque([root]), []
        while queue:
            cur = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                cur = max(cur, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur)
        return ans


if __name__ == '__main__':
    Solution.largestValues([1, 3, 2, 5, 3, null, 9])
