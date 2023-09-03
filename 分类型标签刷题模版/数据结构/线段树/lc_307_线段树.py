
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/13 20:53

'''ST：Segment Tree 线段树'''
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.tree = [0] * n + nums  # 线段树ST长度为2n
        for i in range(n - 1, 0, -1):  # [1, n-1] 倒序添加，子节点之和
            # ST[2i]和ST[2i+1]分别为ST[i]的左右子节点
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n  # nums下标转换到ST下标
        delta = val - self.tree[i]  # 变更值
        while i:  # 自下而上进行更新
            self.tree[i] += delta
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        i, j = left + self.n, right + self.n  # nums下标转换到ST下标
        summ = 0
        while i <= j:
            if i % 2 == 1:  # ST[i]是右子节点
                summ += self.tree[i]  # 计入ST[i]，并i+1（转向下一个区间）
                i += 1
            if j % 2 == 0:  # ST[j]是左子节点
                summ += self.tree[j]  # 计入ST[j]，并j-1（转向上一个区间）
                j -= 1
            i, j = i // 2, j // 2
        return summ

