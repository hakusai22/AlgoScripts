package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/01 13:37
*/

/*
 * 1. 删除操作 把a[i]删除后a[1~i]和b[1~j]匹配
 * 	那a[1~(i-1)]和b[1~j]匹配
 * 	f[i-1][j]+1
 * 2.插入操作
 * 	插入a[i]之后和b[j]匹配
 *   f[i][j-1]+1
 * 3.替换操作把a[i]改成b[j]之后想要a[1~i]与b[1~j]匹配
 * 	那么修改这一位之前，a[1~(i-1)]应该与b[1~(j-1)]匹配
 * 	若 a[i]!=b[j]
 *  f[i-1][j-1] + 1
 *      若a[i]==b[j]
 *  f[i-1]=f[j-1]
 *
 */

const N = 1010

func main() {
	n, m := 0, 0
	var a, b string
	fmt.Scanln(&n)
	fmt.Scanln(&a)
	fmt.Scanln(&m)
	fmt.Scanln(&b)
	var dp [N][N]int
	a = fmt.Sprint(" ", a)
	b = fmt.Sprint(" ", b)

	for i := 0; i <= n; i++ {
		dp[i][0] = i
	}
	for i := 0; i <= m; i++ {
		dp[0][i] = i
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
			if a[i] == b[j] {
				dp[i][j] = min(dp[i][j], dp[i-1][j-1])
			} else {
				dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
			}
		}
	}
	fmt.Println(dp[n][m])
}

//func min(a, b int) int {
//	if a <= b {
//		return a
//	}
//	return b
//}
