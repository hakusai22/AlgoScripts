package SlidingWindow_TwoPointer

import (
	"math"
	"sort"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 15:53
    @题目     : https://leetcode.cn/problems/3sum-closest/description/
    @参考     : https://leetcode.cn/problems/3sum-closest/solutions/2337801/ji-zhi-you-hua-ji-yu-san-shu-zhi-he-de-z-qgqi/
    @时间复杂度: O(n^2)，其中 n 为 nums 的长度。排序 O(nlogn)
    @空间复杂度: O(1)，仅用到若干变量（忽略排序的栈开销）。

 数据范围:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
*/

func threeSumClosest(nums []int, target int) (ans int) {
	sort.Ints(nums)
	n := len(nums)
	minDiff := math.MaxInt
	for i, x := range nums[:n-2] {
		if i > 0 && x == nums[i-1] {
			continue // 优化三
		}

		// 优化一
		s := x + nums[i+1] + nums[i+2]
		if s > target { // 后面无论怎么选，选出的三个数的和不会比 s 还小
			if s-target < minDiff {
				ans = s // 由于下面直接 break，这里无需更新 minDiff
			}
			break
		}

		// 优化二
		s = x + nums[n-2] + nums[n-1]
		if s < target { // x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
			if target-s < minDiff {
				minDiff = target - s
				ans = s
			}
			continue
		}

		// 双指针
		j, k := i+1, n-1
		for j < k {
			s = x + nums[j] + nums[k]
			if s == target {
				return target
			}
			if s > target {
				if s-target < minDiff { // s 与 target 更近
					minDiff = s - target
					ans = s
				}
				k--
			} else { // s < target
				if target-s < minDiff { // s 与 target 更近
					minDiff = target - s
					ans = s
				}
				j++
			}
		}
	}
	return ans
}
