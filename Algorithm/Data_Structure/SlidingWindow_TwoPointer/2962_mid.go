package SlidingWindow_TwoPointer

import "slices"

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/09 15:05
    @题目     : https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
    @参考     : https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/solutions/2560940/hua-dong-chuang-kou-fu-ti-dan-pythonjava-xvwg/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。
    @空间复杂度: O(1)。

 数据范围:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5
*/

func countSubarrays2(nums []int, k int) int64 {
	mx := slices.Max(nums)
	cntMx, left := 0, 0
	ans := int64(0)
	for _, x := range nums {
		if x == mx {
			cntMx++
		}
		for cntMx == k {
			if nums[left] == mx {
				cntMx--
			}
			left++
		}
		ans += int64(left)
	}
	return ans
}
