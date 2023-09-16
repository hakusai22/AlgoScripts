package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/16 11:44
*/

func rob(nums []int) int {
	cur, pre := 0, 0
	for _, x := range nums {
		cur, pre = max(pre+x, cur), cur
	}
	return cur
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
