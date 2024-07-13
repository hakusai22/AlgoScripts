# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/21 09:14
#
# 设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。
# 当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
# 例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
# 实现 StockSpanner 类：
# StockSpanner() 初始化类对象。
# int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。

class StockSpanner:
    def __init__(self):
        self.stk = []

    # 单调递减
    def next(self, price: int) -> int:
        cnt = 1
        while self.stk and self.stk[-1][0] <= price:
            cnt += self.stk.pop()[1]
        self.stk.append((price, cnt))
        return cnt

