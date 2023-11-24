package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/31 15:45
*/

/*
  有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
  第 i 件物品的体积是 vi，价值是 wi。
  求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
  输出最大价值。
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
		n, m    int
		f, v, w [N]int
	)
	fmt.Scanf("%d%d", &n, &m)

	for i := 1; i <= n; i++ {
		fmt.Scanf("%d%d", &n, &m)
	}

	for i := 1; i <= n; i++ {
		for j := m; j >= v[i]; j++ {
			f[j] = max(f[j], f[j-v[i]+w[i]])
		}
	}
	fmt.Printf("%d", f[m])
}
