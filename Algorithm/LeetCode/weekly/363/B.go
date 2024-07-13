package _63

import "sort"

/*
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/09/18 22:26
*/
func countWays(nums []int) int {
	sort.Ints(nums)
	ans := 0
	if nums[0] > 0 {
		ans += 1
	}
	for i, x := range nums[:len(nums)-1] {
		if x < i+1 && i+1 < nums[i+1] {
			ans += 1
		}
	}
	if nums[len(nums)-1] < len(nums) {
		ans += 1
	}
	return ans
}
