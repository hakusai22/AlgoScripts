# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/29 08:19
from python3语法基础.Py流式.py_itertools import accumulate
from typing import List

# 这是一道区间覆盖题目。可以使用差分数组很容易地统计出每个点最终是多少座位。
# 在差分数组中，我们将进来的预订点加上该座位，离开的预订点(因为包含所以错位)减去该座位。
# 最后我们从头到尾遍历，根据差分数组统计每个点最终的值。

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        return list(accumulate(diff))
