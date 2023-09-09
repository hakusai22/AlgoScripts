package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/31 16:41
*/

func main() {

	const N int = 1010

	var (
		// n 数量 m体积
		n, m int
		v, w [N]int
		f    [N]int
	)

	input := bufio.NewReader(os.Stdin)
	fmt.Fscan(input, &n, &m)
	// 从1开始计数
	for i := 1; i <= n; i++ {
		fmt.Fscan(input, &v[i], &w[i])
	}

	for i := 1; i <= n; i++ {
		// 这里因为需要的数据是第i层的数据，所有只需要正序来实现即可
		for j := v[i]; j <= m; j++ {
			// 需要判断不要超过体积j
			f[j] = max(f[j], f[j-v[i]]+w[i])
		}
	}
	fmt.Println(f[m])
}
