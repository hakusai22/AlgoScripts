package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/17 21:49
*/

func rob2(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return max(robRange(nums[1:]), robRange(nums[:n-1]))
}

func robRange(nums []int) int {
	cur, pre := 0, 0
	for _, x := range nums {
		cur, pre = max(pre+x, cur), cur
	}
	return cur
}
