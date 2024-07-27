package _024_07

import (
	"math"
	"slices"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/26 19:32
   @题目     :
   @参考     :
   @时间复杂度:
*/

func findValueOfPartition(nums []int) int {
	slices.Sort(nums)
	ans := math.MaxInt
	for i := 1; i < len(nums); i++ {
		ans = min(ans, nums[i]-nums[i-1])
	}
	return ans
}
