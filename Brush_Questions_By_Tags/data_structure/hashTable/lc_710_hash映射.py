# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 01:28

# 随机取数的时候，只选择[0, n - len(blacklist))，只有这么多不在黑名单的元素。
# 按照这个思路当然有可能对应index下的元素在黑名单里，那么就需要构建一个映射关系，
# 每个[0, n - len(blacklist))里的黑名单元素，与[n - len(blacklist), n)的非黑名单元素构建一个映射关系就行了。
import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.sz = n - len(blacklist)
        last = n - 1

        self.n = n
        self.mapping = {}
        # 下面这步是为了更快判断last是否在blacklist里
        # 如果直接判断元素a是否在list中，时间复杂度为O(n)，在这道题中会超时
        for b in blacklist:
            self.mapping[b] = 666

        for b in blacklist:
            # 如果b在[self.sz, n)里，则跳过，不需要映射了
            if b >= self.sz:
                continue
            while last in self.mapping:
                last -= 1
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        # 随机数的范围为[0, n - len(blacklist))，左闭右开区间
        index = random.randrange(self.sz)
        if index in self.mapping:
            return self.mapping[index]
        return index
