package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 19:42
    @题目     : https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
    @参考     : https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/solutions/2048811/ni-xiang-si-wei-pythonjavacgo-by-endless-b4jt/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。虽然写了个二重循环，但是 left++ 的执行次数不会超过 n 次，所以总的时间复杂度为 O(n)。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
*/

// 把问题转换成「从 nums 中移除一个最长的子数组，使得剩余元素的和为 x」。
func minOperations(nums []int, x int) int {
	target := -x
	for _, x := range nums {
		target += x
	}
	if target < 0 {
		return -1
	}

	ans, left, sum := -1, 0, 0
	for right, x := range nums {
		sum += x
		for sum > target {
			sum -= nums[left]
			left++
		}
		if sum == target {
			ans = max(ans, right-left+1)
		}
	}
	if ans < 0 {
		return -1
	}
	return len(nums) - ans
}
