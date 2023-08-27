package main

import "fmt"

func minimumPossibleSum(n int, target int) int64 {
	nums := make(map[int]bool)
	var sum int64
	sum = 0
	count := 0
	for i := 1; count < n; i++ {
		if nums[target-i] {
			continue
		}
		nums[i] = true
		sum += int64(i)
		count += 1
	}
	return sum
}

func main() {
	fmt.Println(minimumPossibleSum(16, 6)) // 输出 1
}
