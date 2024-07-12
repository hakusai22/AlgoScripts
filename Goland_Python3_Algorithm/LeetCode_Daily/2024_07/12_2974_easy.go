package _024_07

import "slices"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/13 01:43
   @题目     : https://leetcode.cn/problems/minimum-number-game/solutions/2577915/pai-xu-hou-liang-liang-jiao-huan-pythonj-udxc/?envType=daily-question&envId=2024-07-12
   @参考     : https://leetcode.cn/problems/minimum-number-game/solutions/2577915/pai-xu-hou-liang-liang-jiao-huan-pythonj-udxc/?envType=daily-question&envId=2024-07-12
   @时间复杂度:
*/

func numberGame(nums []int) []int {
	slices.Sort(nums)
	for i := 1; i < len(nums); i += 2 {
		nums[i-1], nums[i] = nums[i], nums[i-1]
	}
	return nums
}
