package main

import "fmt"

/*
-*- coding: utf-8 -*-
@Author  : wheat
@Time    : 2023/01/31 15:33
*/
func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func main() {
	const N int = 110
	var (
		n, m    int
		v, w, s [N]int
		f       [N][N]int
	)

	fmt.Scanf("%d%d", &n, &m)
	for i := 1; i <= n; i++ {
		fmt.Scanf("%d%d%d", &v[i], &w[i], &s[i])
	}

	for i := 1; i <= n; i++ {
		for j := 0; j <= m; j++ {
			for k := 0; k <= s[i] && k <= j/v[i]; k++ {
				f[i][j] = max(f[i][j], f[i-1][j-v[i]*k]+w[i]*k)
			}
		}
	}
	fmt.Printf("%d", f[n][m])
}
