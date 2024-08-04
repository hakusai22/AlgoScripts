package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 19:36
    @题目     : https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/
    @参考     : https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/solutions/1988198/tu-jie-yi-ci-bian-li-jian-ji-xie-fa-pyth-n75l/
    @时间复杂度: O(n)，其中 n 为 nums 的长度。
    @空间复杂度: O(1)，仅用到若干额外变量。

 数据范围:
提示：
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9
*/

func numSubarrayBoundedMax(nums []int, left int, right int) int {
	i0, i1 := -1, -1
	ans := 0
	for i, x := range nums {
		if x > right {
			i0 = i
		}
		if x >= left {
			i1 = i
		}
		ans += i1 - i0
	}
	return ans
}
