# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/22 23:25
from typing import List


class Solution:
    def lakeCount(self, field: List[str]) -> int:
        def dfs(x, y):
            # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
            nonlocal di, n, m, vis, field
            vis[x][y] = True
            for ix, iy in di:
                u = x + ix
                v = y + iy
                if 0 <= u and u < n and 0 <= v and v < m and field[u][v] == 'W' and not vis[u][v]:
                    dfs(u, v)

        di = ((1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1))
        n = len(field)
        m = len(field[0])
        # 定义二维列表 初始化False
        vis = [[False for j in range(m)] for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] or field[i][j] != 'W':
                    continue
                ans += 1
                dfs(i, j)
        return ans
