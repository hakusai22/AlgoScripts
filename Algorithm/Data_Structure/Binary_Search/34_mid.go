package main

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/10 13:30
    @题目     : https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
    @参考     : https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/1980196/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-t9l9/
    @时间复杂度: O(logn)，其中 n 为 nums 的长度。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
*/

func searchRange2(nums []int, target int) []int {
	start := lowerBound(nums, target) // 使用其中一种写法即可
	if start == len(nums) || nums[start] != target {
		return []int{-1, -1} // nums 中没有 target
	}
	// 如果 start 存在，那么 end 必定存在
	end := lowerBound(nums, target+1) - 1
	return []int{start, end}
}
