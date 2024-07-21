package _024_07

import "math"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/21 11:44
   @题目     : https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/description/?envType=daily-question&envId=2024-07-21
   @参考     : https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/submissions/548402020/?envType=daily-question&envId=2024-07-21
   @时间复杂度: 时间复杂度：O(n)，其中 n 为 arr 的长度。
*/

func maximumSum(arr []int) int {
	memo := make([][2]int, len(arr))
	for i := range memo {
		memo[i] = [2]int{math.MinInt, math.MinInt}
	}

	var dfs func(int, int) int
	dfs = func(i int, j int) (res int) {
		if i < 0 {
			return math.MinInt / 2
		}
		p := &memo[i][j]
		if *p != math.MinInt {
			return *p
		}

		defer func() {
			*p = res
		}()
		if j == 0 {
			return max(dfs(i-1, 0), 0) + arr[i]
		}
		return max(dfs(i-1, 1)+arr[i], dfs(i-1, 0))
	}
	ans := math.MinInt
	for i := range arr {
		ans = max(ans, dfs(i, 0), dfs(i, 1))
	}
	return ans
}
