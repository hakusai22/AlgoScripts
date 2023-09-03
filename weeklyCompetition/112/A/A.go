package main

import (
	"fmt"
	"math"
)

func minOperationsToSpecialNumber(num string) int {
	n := len(num)
	minOperations := n // 最坏情况下，需要删除所有数字
	for i := n - 1; i >= 0; i-- {
		for j := i - 1; j >= 0; j-- {
			if isSpecial(num[i], num[j]) {
				minOperations = int(math.Min(float64(minOperations), float64(i+n-j-2)))
			}
		}
	}
	return minOperations
}

func isSpecial(a, b byte) bool {
	if a == '0' && b == '0' { // 特殊情况：00
		return true
	}
	if (a == '2' && b == '5') || (a == '5' && b == '0') || (a == '7' && b == '5') || (a == '0' && b == '0') {
		return true
	}
	return false
}

func main() {
	num1 := "2245047"
	result1 := minOperationsToSpecialNumber(num1)
	fmt.Println(result1) // 输出 2

	num2 := "2908305"
	result2 := minOperationsToSpecialNumber(num2)
	fmt.Println(result2) // 输出 3

	num3 := "10"
	result3 := minOperationsToSpecialNumber(num3)
	fmt.Println(result3) // 输出 1
}
