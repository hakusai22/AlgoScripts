package SlidingWindow_TwoPointer

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 15:31
   @题目     : https://leetcode.cn/problems/container-with-most-water/
   @参考     : https://leetcode.cn/problems/container-with-most-water/solutions/1974355/by-endlesscheng-f0xz/
   @时间复杂度: O(n)，其中 n 为 height 的长度。
   @空间复杂度: O(1)，仅用到若干额外变量。
*/

func maxArea(height []int) int {
	left, right := 0, len(height)-1
	ans := 0
	for left < right {
		area := (right - left) * min(height[left], height[right])
		ans = max(ans, area)
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return ans
}
