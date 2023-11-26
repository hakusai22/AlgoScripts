package _18_1126_3

import "math"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/26 18:39
*/
func minimumCoins(prices []int) int {
	n := len(prices)
	memo := make([]int, (n+1)/2)
	var dfs func(int) int
	dfs = func(i int) int {
		if i*2 >= n {
			return prices[i-1] // i 从 1 开始
		}
		p := &memo[i]
		if *p != 0 { // 之前算过
			return *p
		}
		res := math.MaxInt
		for j := i + 1; j <= i*2+1; j++ {
			res = min(res, dfs(j))
		}
		res += prices[i-1]
		*p = res // 记忆化
		return res
	}
	return dfs(1)
}
