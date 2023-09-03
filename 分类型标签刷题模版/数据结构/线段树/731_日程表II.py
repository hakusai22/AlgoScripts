# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/30 08:39

class SegmentTree:
    def __init__(self, u, v):
        self.u, self.v = u, v
        self.c = self.max = 0
        self.__left = self.__right = None

    @property
    def mid(self):
        return (self.u + self.v) // 2

    @property
    def left(self):
        self.__left = self.__left or SegmentTree(self.u, self.mid)
        return self.__left

    @property
    def right(self):
        self.__right = self.__right or SegmentTree(self.mid + 1, self.v)
        return self.__right

    def __push(self):
        self.left.c += self.c
        self.right.c += self.c
        self.max += self.c
        self.c = 0

    def update(self, u, v, x):
        if u <= self.u and self.v <= v:
            self.c += x
            return self.max + self.c
        self.__push()
        if u <= self.mid:
            self.max = max(self.max, self.left.update(u, v, x))
        if self.mid < v:
            self.max = max(self.max, self.right.update(u, v, x))
        return self.max

    def query(self, u, v):
        if u <= self.u and self.v <= v:
            return self.max + self.c
        self.__push()
        res = -float('inf')
        if u <= self.mid:
            res = max(res, self.left.query(u, v))
        if self.mid < v:
            res = max(res, self.right.query(u, v))
        return res


class MyCalendarTwo:

    def __init__(self):
        self.__tree = SegmentTree(0, 10 ** 9)

    def book(self, start: int, end: int) -> bool:
        if self.__tree.query(start, end - 1) >= 2:
            return False
        self.__tree.update(start, end - 1, 1)
        return True
