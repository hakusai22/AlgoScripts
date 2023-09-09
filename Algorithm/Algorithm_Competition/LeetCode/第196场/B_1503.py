# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 22:09

# 问题相乘相遇的蚂蚁是互换了方向，但是互换后的蚂蚁顺序调换一下就可以理解成互相穿过
# 1.如果left数组存在，则需要找最右边(max(left))那个蚂蚁到最左边的(0)的距离dist1。
# 2.如果right数组存在，则需要找最左边(max(right))那个蚂蚁到最右边的(n)的距离dist2。
# 然后return max(dist1, dist2)就完事儿。

# https://leetcode.cn/problems/last-moment-before-all-ants-fall-out-of-a-plank/submissions/
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        if left:
            time = max(time, max(left))
        if right:
            time = max(time, n - min(right))
        return time
