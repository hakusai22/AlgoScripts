# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/3 16:15


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curd = 0
        cx, cy = 0, 0
        while head:
            res[cx][cy] = head.val
            head = head.next
            dx, dy = dirs[curd]
            xx, yy = cx + dx, cy + dy
            if not (0 <= xx < m and 0 <= yy < n and res[xx][yy] == -1):
                curd += 1
                curd %= 4
                dx, dy = dirs[curd]
                xx, yy = cx + dx, cy + dy
            cx, cy = xx, yy
        return res


if __name__ == '__main__':
    print(Solution.spiralMatrix(3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]))
