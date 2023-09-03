package main

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/31 15:33
*/

/**
将物品i的数量拆分成1, 2, 4, 8, … , 2k−1,c
相当于分成一个个组, 然后通过组合的方式必然能凑成0~s[i]的数量
然后做一次01背包问题
时间：O(N * V * log S)
*/

import "fmt"

const N int = 11000 // 物品数量= N * Log S = 1000 * log2000
var (
	n, m    int
	f, v, w [N]int
)

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//	return b
//}

func main() {
	fmt.Scanf("%d%d", &n, &m)

	cnt := 0
	for i := 1; i <= n; i++ {
		var a, b, s int
		fmt.Scanf("%d%d%d", &a, &b, &s)
		k := 1

		for k < s {
			cnt++
			v[cnt] = a * k
			w[cnt] = b * k
			s -= k
			k <<= 1
		}

		if s > 0 {
			cnt++
			v[cnt] = a * s
			w[cnt] = b * s
		}
	}

	n = cnt
	for i := 1; i <= n; i++ {
		for j := m; j >= v[i]; j-- {
			f[j] = max(f[j], f[j-v[i]]+w[i])
		}
	}

	fmt.Printf("%d", f[m])
}
