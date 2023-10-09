# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 20:48
from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/display-table-of-food-orders-in-a-restaurant/submissions/
class Solution:
    def displayTable(orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(lambda: defaultdict(int))
        food_set = set()
        for _, table, food in orders:
            food_set.add(food)
            tables[table][food] += 1

        res = []
        food_list = sorted(food_set)
        res.append(['Table'] + food_list)
        for table in sorted(tables.keys(), key=int):
            res.append([table] + [str(tables[table][item]) for item in food_list])
        return res


if __name__ == '__main__':
    print(
        Solution.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                                   ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
