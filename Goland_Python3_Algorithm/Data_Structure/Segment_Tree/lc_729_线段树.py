
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 12:01

class Node:

    def __init__(self, si, ei):
        self.si = si
        self.ei = ei
        self.mi = si + ei >> 1
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0

class SegmentTree:

    def __init__(self, si, ei):
        self.root = Node(si, ei)

    def pushDown(self, node: Node):
        if not node.left: node.left = Node(node.si, node.mi)
        if not node.right: node.right = Node(node.mi + 1, node.ei)
        if node.lazy == 0: return
        node.left.val += node.lazy
        node.right.val += node.lazy
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0

    def update(self, node: Node, l, r, val):  # 将[l,r]增加val
        if node.ei < l or node.si > r:
            return
        if l <= node.si <= node.ei <= r:
            node.val += val
            node.lazy += val
            return
        self.pushDown(node)
        if node.mi >= l:
            self.update(node.left, l, r, val)
        if node.mi + 1 <= r:
            self.update(node.right, l, r, val)
        node.val = max(node.left.val, node.right.val) # 求最大值

    def query(self, node: Node, l, r):
        if node.ei < l or node.si > r:
            return 0
        if l <= node.si <= node.ei <= r:
            return node.val
        self.pushDown(node)
        ans = 0
        if node.mi >= l:
            ans = max(ans, self.query(node.left, l, r))
        if node.mi + 1 <= r:
            ans = max(ans, self.query(node.right, l, r))
        return ans


class MyCalendar:

    def __init__(self):
        self.st = SegmentTree(0, int(1e9))

    def book(self, start: int, end: int) -> bool:
        local = self.st.query(self.st.root, start, end - 1)
        if local == 1:
            return False
        else:
            self.st.update(self.st.root, start, end - 1, 1)
            return True
