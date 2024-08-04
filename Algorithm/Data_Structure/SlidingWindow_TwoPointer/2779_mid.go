package SlidingWindow_TwoPointer

import "slices"

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 19:23
    @题目     : https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/description/
    @参考     : https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/2345805/pai-xu-shuang-zhi-zhen-by-endlesscheng-hbqx/
    @时间复杂度: 时间复杂度：O(nlogn)，其中 n 为 nums 的长度。瓶颈在排序上。虽然写了个二重循环，但是内层循环中对 left 加一的总执行次数不会超过 n 次，所以滑窗那部分的时间复杂度为 O(n)。
    @空间复杂度: O(1)。忽略排序的栈开销，仅用到若干额外变量。

 数据范围:

*/

func maximumBeauty(nums []int, k int) int {
	slices.Sort(nums)
	left, ans := 0, 0
	for right, x := range nums {
		for x-nums[left] > k*2 {
			left++
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
