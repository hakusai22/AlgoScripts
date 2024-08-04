package SlidingWindow_TwoPointer

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 14:55
   @题目     : https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
   @参考     : https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
   @时间复杂度: 时间复杂度：O(n)，其中 n 为 numbers 的长度。 空间复杂度：O(1)，仅用到若干额外变量。
*/

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for {
		s := numbers[left] + numbers[right]
		if s == target {
			return []int{left + 1, right + 1}
		}
		if s > target {
			right--
		} else {
			left++
		}
	}
}
