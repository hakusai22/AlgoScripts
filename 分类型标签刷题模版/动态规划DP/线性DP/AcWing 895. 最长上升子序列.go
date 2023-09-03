package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/01 11:12
*/

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//	return b
//}

func main() {
	const N int = 1010

	var a, f [N]int

	var n int
	fmt.Scanf("%d", &n)
	for i := 1; i <= n; i++ {
		fmt.Scanf("%d", &a[i])
	}
	for i := 1; i <= n; i++ {
		f[i] = 1

		for j := 1; j < i; j++ {
			if a[j] < a[i] {
				f[i] = max(f[i], f[j]+1)
			}
		}
	}
	res := 0
	for i := 1; i <= n; i++ {
		res = max(res, f[i])
	}
	fmt.Printf("%d", res)
}
