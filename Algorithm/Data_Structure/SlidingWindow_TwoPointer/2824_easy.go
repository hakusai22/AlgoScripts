package SlidingWindow_TwoPointer

import "sort"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 15:16
   @题目     : https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/description/
   @参考     : https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/solutions/2396216/onlogn-pai-xu-shuang-zhi-zhen-by-endless-qk40/
   @时间复杂度: O(nlogn)，其中 n 为 nums 的长度。瓶颈在排序上
   @空间复杂度: O(1)。不计入排序的栈开销，仅用到若干额外变量。
*/

func countPairs(nums []int, target int) int {
	sort.Ints(nums)
	left, right := 0, len(nums)-1
	ans := 0
	for left < right {
		if nums[left]+nums[right] < target {
			ans += right - left
			left++
		} else {
			right--
		}
	}
	return ans
}
