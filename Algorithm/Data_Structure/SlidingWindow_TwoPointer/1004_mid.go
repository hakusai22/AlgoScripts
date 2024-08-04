package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 19:31
    @题目     : https://leetcode.cn/problems/max-consecutive-ones-iii/description/
    @参考     : https://leetcode.cn/problems/max-consecutive-ones-iii/solutions/2126631/hua-dong-chuang-kou-yi-ge-shi-pin-jiang-yowmi/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:

*/

func longestOnes(nums []int, k int) int {
	left, cnt0 := 0, 0
	ans := 0
	for right, x := range nums {
		cnt0 += 1 - x
		for cnt0 > k {
			cnt0 -= 1 - nums[left]
			left++
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
