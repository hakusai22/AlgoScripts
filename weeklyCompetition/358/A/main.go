package main

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 12:58
*/

func maxSum(nums []int) int {
	maxSum := -1

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if getMaxDigit(nums[i]) == getMaxDigit(nums[j]) {
				maxSum = max(maxSum, nums[i]+nums[j])
			}
		}
	}

	return maxSum
}

func getMaxDigit(num int) int {
	maxDigit := 0
	for num > 0 {
		digit := num % 10
		if digit > maxDigit {
			maxDigit = digit
		}
		num /= 10
	}
	return maxDigit
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	maxSum([]int{51, 71, 17, 24, 42})
}
