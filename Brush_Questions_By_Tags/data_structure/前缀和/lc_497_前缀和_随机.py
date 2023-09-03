# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/9 09:19

import bisect
import random
from typing import List


def __init__(rects: List[List[int]]):
    rects = rects
    presum = [0]
    for a, b, x, y in rects:
        presum.append(presum[-1] + (x - a + 1) * (y - b + 1))


def pick() -> List[int]:
    rdm = random.randint(0, presum[-1] - 1)
    idx = bisect.bisect_right(presum, rdm) - 1
    a, b, x, y = rects[idx]
    v = rdm - presum[idx]
    return [a + v % (w := x - a + 1), b + v // w]


if __name__ == '__main__':
    print(__init__([[-2, -2, -1, -1], [1, 0, 3, 0]]))
    print(pick())
