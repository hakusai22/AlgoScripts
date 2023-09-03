package interval_dp

import (
	"bufio"
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/02 14:37
*/

/**
 """
    题意：合并 N 堆石子，每次只能合并相邻的两堆石子，求最小代价
    关键点：最后一次合并一定是左边连续的一部分和右边连续的一部分进行合并

    状态表示：f[i][j] 表示将 i 到 j 这一段石子合并成一堆的方案的集合，
    属性 Min
    前缀和数组 a[i]=a[i−1]+x[i] x[i-j]=a[j]−a[i−1]
    状态转移方程式:
        f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]+a[j]−a[i−1])
    枚举顺序：
        很明显，长的区间由短的区间合并而成
        所以先枚举区间长度 len 接着枚举左端点 l(右端点由左端点和区间长度去确定)
        最后枚举分段点 k，计算 dp 方程
"""
*/

func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func main() {

	const N int = 310
	const Max int = 0x3f3f3f3f

	var (
		s [N]int
		f [N][N]int
	)
	input := bufio.NewReader(os.Stdin)

	var n int
	fmt.Scanf("%d", &n)

	for i := 1; i <= n; i++ {
		fmt.Fscan(input, &s[i])
		// 前缀和
		s[i] += s[i-1]
	}
	// 通过区间长度来计算
	for len := 2; len <= n; len++ {
		// 右边界需要小于n
		for i := 1; i+len-1 <= n; i++ {
			// 枚举区间起始点
			l, r := i, i+len-1
			f[l][r] = Max
			for k := l; k <= r-1; k++ {
				f[l][r] = min(f[l][r], f[l][k]+f[k+1][r]+s[r]-s[l-1])
			}
		}
	}

	fmt.Println(f[1][n])
}
