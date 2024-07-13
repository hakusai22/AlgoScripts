package _69_1126_3

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/26 16:18
*/
func findKOr(nums []int, k int) (ans int) {
	for i := 0; i < 31; i++ {
		cnt1 := 0
		for _, x := range nums {
			cnt1 += x >> i & 1
		}
		if cnt1 >= k {
			ans |= 1 << i
		}
	}
	return
}
