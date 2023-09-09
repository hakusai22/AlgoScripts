package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/01 17:32
*/

func edit_distance(a, b string) int {

	var f [N][N]int

	// 注意
	m, n := len(a)-1, len(b)-1
	for i := 0; i <= m; i++ {
		f[i][0] = i
	}
	for i := 0; i <= n; i++ {
		f[0][i] = i
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			f[i][j] = min(f[i-1][j]+1, f[i][j-1]+1)
			if a[i] == b[j] {
				f[i][j] = min(f[i][j], f[i-1][j-1])
			} else {
				f[i][j] = min(f[i][j], f[i-1][j-1]+1)
			}
		}
	}
	return f[m][n]
}

func main() {
	const N int = 1010
	var s [N]string

	var n, m, x int
	fmt.Scan(&n, &m)
	for i := 0; i < n; i++ {
		fmt.Scan(&s[i])
	}
	var t string
	for i := 0; i < m; i++ {
		fmt.Scan(&t, &x)
		t = " " + t
		cnt := 0
		for j := 0; j < n; j++ {
			o := " " + s[j]
			if edit_distance(o, t) <= x {
				cnt++
			}
		}
		fmt.Println(cnt)
	}
}

//func min(a, b int) int {
//	if a < b {
//		return a
//
//	}
//	return b
//}
