package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 15:50
    @题目     :
    @参考     : https://leetcode.cn/problems/minimum-size-subarray-sum/solutions/1959532/biao-ti-xia-biao-zong-suan-cuo-qing-kan-k81nh/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
*/

func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	ans, sum, left := n+1, 0, 0
	for right, x := range nums {
		sum += x
		for sum-nums[left] >= target {
			sum -= nums[left]
			left++
		}
		if sum >= target {
			ans = min(ans, right-left+1)
		}
	}
	if ans <= n {
		return ans
	}
	return 0
}
