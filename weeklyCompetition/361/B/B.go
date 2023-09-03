package main

import (
	"fmt"
	"strings"
)

func minimumOperations(num string) int {
	ans := len(num)
	if strings.Contains(num, "0") {
		ans--
	}
	f := func(tail string) {
		i := strings.LastIndexByte(num, tail[1])
		if i < 0 {
			return
		}
		i = strings.LastIndexByte(num[:i], tail[0])
		if i < 0 {
			return
		}
		ans = min(ans, len(num)-i-2)
	}
	f("00")
	f("25")
	f("50")
	f("75")
	return ans
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}

func main() {
	num1 := "2245047"
	result1 := minimumOperations(num1)
	fmt.Println(result1) // 输出 2

	num2 := "2908305"
	result2 := minimumOperations(num2)
	fmt.Println(result2) // 输出 3

	num3 := "10"
	result3 := minimumOperations(num3)
	fmt.Println(result3) // 输出 1
}
