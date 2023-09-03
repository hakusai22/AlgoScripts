package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/01 13:30
*/

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//
//	return b
//}

func main() {
	const N int = 1010
	var (
		n, m int
		s, p [N]byte
		f    [N][N]int
	)

	fmt.Scanf("%d%d\n", &n, &m)

	for i := 1; i <= n; i++ {
		fmt.Scanf("%c", &s[i])
	}
	fmt.Scanf("\n")
	for i := 1; i <= m; i++ {
		fmt.Scanf("%c", &p[i])
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			f[i][j] = max(f[i-1][j], f[i][j-1])
			if s[i] == p[j] {
				f[i][j] = max(f[i][j], f[i-1][j-1]+1)
			}
		}
	}

	fmt.Printf("%d", f[n][m])
}
