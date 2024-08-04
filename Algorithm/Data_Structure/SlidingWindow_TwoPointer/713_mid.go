package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 15:55
    @题目     : https://leetcode.cn/problems/subarray-product-less-than-k/
    @参考     : https://leetcode.cn/problems/subarray-product-less-than-k/solutions/1959538/xia-biao-zong-suan-cuo-qing-kan-zhe-by-e-jebq/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。虽然写了个二重循环，但是内层循环中对 left 加一的总执行次数不会超过 n 次，所以总的时间复杂度为 O(n)。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
*/

func numSubarrayProductLessThanK(nums []int, k int) int {
	ans := 0
	if k <= 1 {
		return ans
	}
	prod, left := 1, 0
	for right, x := range nums {
		prod *= x
		for prod >= k {
			prod /= nums[left]
			left++
		}
		ans += right - left + 1
	}
	return ans
}
