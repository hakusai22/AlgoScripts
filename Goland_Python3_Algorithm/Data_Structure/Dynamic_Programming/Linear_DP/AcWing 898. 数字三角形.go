package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/01 11:09
*/

var rr = bufio.NewReader(os.Stdin)

var a, f [510][510]int

func main() {
	var n int
	fmt.Fscan(rr, &n)
	for i := 0; i < n; i++ {
		for j := 0; j <= i; j++ {
			fmt.Fscan(rr, &a[i][j])
			f[i][j] = a[i][j]
		}
	}

	// f[i][j]: 从最后一层走到(i, j)的最大路径和
	// f[i][j] = max(f[i+1][j], f[i+1][j+1]) + a[i][j]
	for i := n - 1; i >= 0; i-- {
		for j := 0; j <= i; j++ {
			f[i][j] = max(f[i+1][j], f[i+1][j+1]) + a[i][j]
		}
	}
	fmt.Println(f[0][0])
}

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//	return b
//}
