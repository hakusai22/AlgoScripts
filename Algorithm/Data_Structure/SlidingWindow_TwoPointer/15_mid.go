package SlidingWindow_TwoPointer

import "sort"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 15:01
   @题目     : https://leetcode.cn/problems/3sum/description/
   @参考     : https://leetcode.cn/problems/3sum/solutions/1968332/shuang-zhi-zhen-xiang-bu-ming-bai-yi-ge-pno55/
   @时间复杂度: 时间复杂度：O(n^2)，其中 n 为 nums 的长度。排序 O(nlogn)。
	空间复杂度：O(1)，仅用到若干变量（忽略排序的栈开销）。
*/

func threeSum(nums []int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	for i, x := range nums[:n-2] {
		if i > 0 && x == nums[i-1] {
			continue
		}
		if x+nums[i+1]+nums[i+2] > 0 {
			break
		}
		if x+nums[n-2]+nums[n-1] < 0 {
			continue
		}
		j, k := i+1, n-1
		for j < k {
			s := x + nums[j] + nums[k]
			if s > 0 {
				k--
			} else if s < 0 {
				j++
			} else {
				ans = append(ans, []int{x, nums[j], nums[k]})
				for j++; j < k && nums[j] == nums[j-1]; j++ {
				} // 跳过重复数字
				for k--; k > j && nums[k] == nums[k+1]; k-- {
				} // 跳过重复数字
			}
		}
	}
	return
}
