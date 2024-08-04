package SlidingWindow_TwoPointer

import (
	"slices"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 15:19
   @题目     : https://leetcode.cn/problems/valid-triangle-number/
   @参考     : https://leetcode.cn/problems/valid-triangle-number/solutions/2432875/zhuan-huan-cheng-abcyong-xiang-xiang-shu-1ex3/
   @时间复杂度: O(n^2)，其中 n 为 nums 的长度。
   @空间复杂度: O(1)。不计入排序的栈开销，仅用到若干额外变量。
*/

func triangleNumber(nums []int) int {
	//  sort.Ints(nums)
	slices.Sort(nums)
	ans := 0
	for k := 2; k < len(nums); k++ {
		c := nums[k]
		i := 0
		j := k - 1
		for i < j {
			if nums[i]+nums[j] > c {
				ans += j - i
				j--
			} else {
				i++
			}
		}
	}
	return ans
}
