package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 15:59
    @题目     : https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
    @参考     : https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/solutions/2560708/hua-dong-chuang-kou-fu-ti-dan-pythonjava-6fxo/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。
    @空间复杂度: O(n)。

 数据范围:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
*/

func maxSubarrayLength(nums []int, k int) int {
	cnt := map[int]int{}
	left := 0
	ans := 0
	for right, x := range nums {
		cnt[x]++
		for cnt[x] > k {
			cnt[nums[left]]--
			left++
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
