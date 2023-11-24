package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/31 17:36
*/

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//	return b
//}

func main() {
	const N, M int = 110, 110
	var (
		n, m int
		v, w [N][M]int
		f, s [N]int
	)

	fmt.Scanf("%d%d", &n, &m)
	for i := 1; i <= n; i++ {
		fmt.Scanf("%d", &s[i])
		for j := 1; j <= s[i]; j++ {
			fmt.Scanf("%d%d", &v[i][j], &w[i][j])
		}
	}

	for i := 1; i <= n; i++ {
		for j := m; j >= 0; j-- {
			for k := 0; k <= s[i]; k++ {
				if j >= v[i][k] {
					f[j] = max(f[j], f[j-v[i][k]]+w[i][k])
				}
			}
		}
	}

	fmt.Printf("%d", f[m])
}
