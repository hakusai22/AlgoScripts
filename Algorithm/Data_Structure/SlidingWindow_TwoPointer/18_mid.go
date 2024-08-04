package SlidingWindow_TwoPointer

import "sort"

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 15:48
    @题目     : https://leetcode.cn/problems/4sum/description/
    @参考     : https://leetcode.cn/problems/4sum/solutions/2344514/ji-zhi-you-hua-ji-yu-san-shu-zhi-he-de-z-1f0b/
    @时间复杂度: O(n^3)，其中 n 为 nums 的长度。排序 O(nlogn)。
    @空间复杂度: O(1)。忽略返回值和排序的栈开销，仅用到若干变量。

 数据范围:
提示：
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

*/

func fourSum(nums []int, target int) (ans [][]int) {
	sort.Ints(nums)
	n := len(nums)
	for a := 0; a < n-3; a++ { // 枚举第一个数
		x := nums[a]
		if a > 0 && x == nums[a-1] { // 跳过重复数字
			continue
		}
		if x+nums[a+1]+nums[a+2]+nums[a+3] > target { // 优化一
			break
		}
		if x+nums[n-3]+nums[n-2]+nums[n-1] < target { // 优化二
			continue
		}
		for b := a + 1; b < n-2; b++ { // 枚举第二个数
			y := nums[b]
			if b > a+1 && y == nums[b-1] { // 跳过重复数字
				continue
			}
			if x+y+nums[b+1]+nums[b+2] > target { // 优化一
				break
			}
			if x+y+nums[n-2]+nums[n-1] < target { // 优化二
				continue
			}
			c, d := b+1, n-1
			for c < d { // 双指针枚举第三个数和第四个数
				s := x + y + nums[c] + nums[d] // 四数之和
				if s > target {
					d--
				} else if s < target {
					c++
				} else {
					ans = append(ans, []int{x, y, nums[c], nums[d]})
					for c++; c < d && nums[c] == nums[c-1]; c++ {
					} // 跳过重复数字
					for d--; d > c && nums[d] == nums[d+1]; d-- {
					} // 跳过重复数字
				}
			}
		}
	}
	return
}
