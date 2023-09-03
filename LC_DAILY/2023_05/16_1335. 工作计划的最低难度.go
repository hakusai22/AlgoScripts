/*
 * @Author: hakusai
 * @Date: 2023-05-16 08:59:28
 * @LastEditTime: 2023-05-16 21:24:39
 */

package _023_05

import "math"

func minDifficulty(a []int, d int) int {
	n := len(a)
	if n < d {
		return -1
	}

	memo := make([][]int, d)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = -1 // -1 表示还没有计算过
		}
	}
	var dfs func(int, int) int
	dfs = func(i, j int) (res int) {
		p := &memo[i][j]
		if *p != -1 { // 之前计算过了
			return *p
		}
		defer func() { *p = res }() // 记忆化
		if i == 0 {                 // 只有一天，必须完成所有工作
			for _, x := range a[:j+1] {
				res = max(res, x)
			}
			return
		}
		res = math.MaxInt
		mx := 0
		for k := j; k >= i; k-- {
			mx = max(mx, a[k]) // 从 a[k] 到 a[j] 的最大值
			res = min(res, dfs(i-1, k-1)+mx)
		}
		return
	}
	return dfs(d-1, n-1)
}
