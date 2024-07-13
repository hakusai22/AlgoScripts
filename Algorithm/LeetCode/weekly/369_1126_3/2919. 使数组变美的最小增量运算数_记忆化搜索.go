package _69_1126_3

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/26 17:42
*/
func minIncrementOperations(nums []int, k int) int64 {
	n := len(nums)
	memo := make([][3]int, n)
	for i := range memo {
		memo[i] = [3]int{-1, -1, -1}
	}
	var dfs func(int, int) int
	dfs = func(i, j int) int {
		if i < 0 {
			return 0
		}
		p := &memo[i][j]
		if *p != -1 {
			return *p
		}
		res := dfs(i-1, 0) + max2(k-nums[i], 0) // nums[i] 增大
		if j < 2 {
			res = min(res, dfs(i-1, j+1)) // nums[i] 不增大
		}
		*p = res
		return res
	}
	return int64(dfs(n-1, 0))
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
func max2(a, b int) int {
	if b > a {
		return b
	}
	return a
}
