# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:41
import bisect

if __name__ == '__main__':
    a = [1, 2, 2, 4, 5]
    p = bisect.bisect(a, 7)
    print(p)

    bisect.insort(a, 4)
    print(a)
    p = bisect.bisect_left(a, 2)
    print(p)
    p = bisect.bisect_right(a, 2)
    print(p)
