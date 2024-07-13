# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 20:56
from typing import List


# 字典是可变容器类型，可以存储任意类型对象。在python中，创建字典，使用{}或者dict()函数。
# 字典中的值是以键值对(key=>value)的形式存在， key和value使用:分割。每个键值对之间用,分割。格式形式如下：
# test_dict = {key1:value1, key2:value2}
# 需要注意的是：
#     1.键是唯一的，如果键出现重复，后面的会替代前面的。
#     2.键的值必须不可变
#     3.值不需要唯一，且值可以是任何类型的。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
