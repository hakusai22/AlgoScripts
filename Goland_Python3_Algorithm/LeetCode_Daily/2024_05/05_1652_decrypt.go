package _024_05

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2024/05/05 00:04
*/

func decrypt(code []int, k int) []int {
	n := len(code)
	ans := make([]int, n)
	if k == 0 {
		return ans
	}
	for i := 0; i < n; i++ {
		if k > 0 {
			for j := i + 1; j < i+k+1; j++ {
				ans[i] += code[j%n]
			}
		} else {
			for j := i + k; j < i; j++ {
				ans[i] += code[(j+n)%n]
			}
		}
	}
	return ans
}
