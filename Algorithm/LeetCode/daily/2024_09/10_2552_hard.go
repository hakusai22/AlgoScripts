package _024_09

import "slices"

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/10 08:57
    @题目     :
    @参考     : https://leetcode.cn/problems/count-increasing-quadruplets/solutions/2080632/you-ji-qiao-de-mei-ju-yu-chu-li-pythonja-exja/
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func countQuadruplets(nums []int) (ans int64) {
	n := len(nums)
	great := make([][]int, n)
	great[n-1] = make([]int, n+1)
	for k := n - 2; k >= 2; k-- {
		great[k] = slices.Clone(great[k+1])
		for x := 1; x < nums[k+1]; x++ {
			great[k][x]++
		}
	}

	less := make([]int, n+1)
	for j := 1; j < n-2; j++ {
		for x := nums[j-1] + 1; x <= n; x++ {
			less[x]++
		}
		for k := j + 1; k < n-1; k++ {
			if nums[j] > nums[k] {
				ans += int64(less[nums[k]] * great[k][nums[j]])
			}
		}
	}
	return
}
