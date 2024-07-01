package Base_DP

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai
   @Time    : 2024/07/02 00:53
	https://leetcode.cn/problems/climbing-stairs/solutions/2560716/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-7zm1/
*/

func climbStairs(n int) int {
	memo := make([]int, n+1)
	var dfs func(int) int
	dfs = func(i int) int {
		if i <= 1 {
			return 1
		}
		p := &memo[i]
		if *p != 0 {
			return *p
		}
		res := dfs(i-1) + dfs(i-2)
		*p = res
		return res
	}
	return dfs(n)
}

func climbStairs2(n int) int {
	f := make([]int, n+1)
	f[0], f[1] = 1, 1
	for i := 2; i <= n; i++ {
		f[i] = f[i-1] + f[i-2]
	}
	return f[n]
}
