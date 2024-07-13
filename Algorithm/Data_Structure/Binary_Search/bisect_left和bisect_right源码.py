# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/11/22 22:34
def bisect_left(a, x, lo=0, hi=None):
    """
    	假设对a排序, 返回将x插入到a中的索引值i, 当遇到重复值时, 按照最左边位置返回
    	使得a[:i]中所有元素都小于x

    	a: list, 假设已经排好序的列表(升序)
    	x: 需要插入的元素
    	lo=0: 二分算法中的low指针位置, 默认0
    	hi=None: 二分算法中的high指针位置, 默认None, 表示len(a)
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(a, x, lo=0, hi=None):
    """
    	假设对a排序, 返回将x插入到a中的索引值i, 当遇到重复值时, 按照最右边位置返回
    	使得a[:i]中所有元素都小于等于x
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
