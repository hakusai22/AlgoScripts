package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/09 14:59
    @题目     : https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/
    @参考     : https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/solutions/1595722/by-endlesscheng-b120/
    @时间复杂度: O(n)，其中 n 是 nums 的长度。
    @空间复杂度: 仅需要几个额外的变量。

 数据范围:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^15
*/

func countSubarrays(nums []int, k int64) int64 {
	sum, left := int64(0), 0
	ans := int64(0)
	for right, num := range nums {
		sum += int64(num)
		for sum*int64(right-left+1) >= k {
			sum -= int64(nums[left])
			left++
		}
		ans += int64(right - left + 1)
	}
	return ans
}
