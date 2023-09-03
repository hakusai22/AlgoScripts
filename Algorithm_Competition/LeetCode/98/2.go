package _8

import (
	"sort"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/19 11:53
*/

func minimizeSum(nums []int) (ans int) {
	sort.Ints(nums)
	n := len(nums)
	ans = nums[n-2] - nums[1]
	ans = min(ans, nums[n-1]-nums[2])
	ans = min(ans, nums[n-3]-nums[0])
	return
}
