package main

import (
	"fmt"
	"sort"
)

func minOperations(nums []int, target int) int {
	if target == 0 {
		return 0
	}

	sort.Sort(sort.Reverse(sort.IntSlice(nums)))

	result := -1

	var dfs func(start, target, count int)
	dfs = func(start, target, count int) {
		if target == 0 {
			if result == -1 || count < result {
				result = count
			}
			return
		}

		if start == len(nums) || target < nums[start] {
			return
		}

		// Take current number
		dfs(start+1, target-nums[start], count+1)

		// Skip current number
		dfs(start+1, target, count)
	}

	dfs(0, target, 0)

	return result
}

func main() {
	nums1 := []int{1, 2, 8}
	target1 := 7
	fmt.Println(minOperations(nums1, target1)) // 输出 1

	nums2 := []int{1, 32, 1, 2}
	target2 := 12
	fmt.Println(minOperations(nums2, target2)) // 输出 2

	nums3 := []int{1, 32, 1}
	target3 := 35
	fmt.Println(minOperations(nums3, target3)) // 输出 -1
}
