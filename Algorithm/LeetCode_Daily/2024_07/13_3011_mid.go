package _024_07

import (
	"math/bits"
	"slices"
)

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai
@Time    : 2024/07/13 01:34
@题目 https://leetcode.cn/problems/find-if-array-can-be-sorted/description/
@参考 https://leetcode.cn/problems/find-if-array-can-be-sorted/solutions/2613051/jiao-ni-yi-ci-xing-ba-dai-ma-xie-dui-on-j3nik/
@时间复杂度：O(nlogn)，其中 n 为 nums 的长度
*/

func canSortArray(nums []int) bool {
	for i, n := 0, len(nums); i < n; {
		start := i
		ones := bits.OnesCount(uint(nums[i]))
		i++
		for i < n && bits.OnesCount(uint(nums[i])) == ones {
			i++
		}
		slices.Sort(nums[start:i])
	}
	return slices.IsSorted(nums)
}
