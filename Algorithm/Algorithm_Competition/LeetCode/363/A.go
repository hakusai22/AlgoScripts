package _63

import "math/bits"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/18 22:20
*/
func sumIndicesWithKSetBits(nums []int, k int) int {
	ans := 0
	for i, x := range nums {
		if bits.OnesCount(uint(i)) == k {
			ans += x
		}
	}
	return ans
}
