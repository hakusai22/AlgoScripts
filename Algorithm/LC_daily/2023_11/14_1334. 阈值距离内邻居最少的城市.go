package _023_11

import "math"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/14 23:07
*/

func findTheCity(n int, edges [][]int, distanceThreshold int) (ans int) {
	w := make([][]int, n)
	for i := range w {
		w[i] = make([]int, n)
		for j := range w[i] {
			w[i][j] = math.MaxInt / 2 // 防止加法溢出
		}
	}
	for _, e := range edges {
		x, y, wt := e[0], e[1], e[2]
		w[x][y], w[y][x] = wt, wt
	}

	memo := make([][][]int, n)
	for i := range memo {
		memo[i] = make([][]int, n)
		for j := range memo[i] {
			memo[i][j] = make([]int, n)
		}
	}
	var dfs func(int, int, int) int
	dfs = func(k, i, j int) int {
		if k < 0 { // 递归边界
			return w[i][j]
		}
		p := &memo[i][j][k]
		if *p != 0 { // 之前计算过
			return *p
		}
		res := min(dfs(k-1, i, j), dfs(k-1, i, k)+dfs(k-1, k, j))
		*p = res // 记忆化
		return res
	}

	minCnt := n
	for i := 0; i < n; i++ {
		cnt := 0
		for j := 0; j < n; j++ {
			if j != i && dfs(n-1, i, j) <= distanceThreshold {
				cnt++
			}
		}
		if cnt <= minCnt { // 相等时取最大的 i
			minCnt = cnt
			ans = i
		}
	}
	return ans
}
