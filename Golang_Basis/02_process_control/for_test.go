package _2_process_control

import (
	"fmt"
	"testing"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 02:07
   @题目     :
   @参考     :
   @时间复杂度:
*/

func TestFor(t *testing.T) {
	s := "abc"

	for i, n := 0, len(s); i < n; i++ { // 常见的 for 循环，支持初始化语句。
		println(s[i])
	}

	var i, j int

	for i = 2; i < 100; i++ {
		for j = 2; j <= (i / j); j++ {
			if i%j == 0 {
				break // 如果发现因子，则不是素数
			}
		}
		if j > (i / j) {
			fmt.Printf("%d  是素数\n", i)
		}
	}

	for { // 替代 while (true) {}
		println(s) // 替代 for (;;) {}
	}
}
