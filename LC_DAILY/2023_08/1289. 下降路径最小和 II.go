/*
 * @Author: hakusai
 * @Date: 2023-08-10 16:34:25
 * @LastEditTime: 2023-08-10 16:43:45
 * @Description: https://github.com/hakusai22
 */
package main

func minFallingPathSum(grid [][]int) int {
	n := len(grid)
	f := make([][]int, n+1)
	for i, _ := range f {
		f[i] = make([]int, n)
	}

	const inf = 1 << 30
	for i, row := range grid {
		i++
		for j, v := range row {
			x := inf
			for k := range row {
				if k != j {
					x = min(x, f[i-1][k])
				}
			}
			if x == inf {
				x = 0
			}
			f[i][j] = v + x
		}
	}
	ans := inf
	for _, v := range f[n] {
		ans = min(ans, v)
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
