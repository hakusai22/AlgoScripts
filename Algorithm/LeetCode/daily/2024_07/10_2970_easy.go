package _024_07

/*
@Author  : https://github.com/hakusai22
@Time    : 2024/07/13 17:57
@题目     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/description/?envType=daily-question&envId=2024-07-10
@参考     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/solutions/2577665/shuang-zhi-zhen-on-shi-jian-o1-kong-jian-3fl2/?envType=daily-question&envId=2024-07-10
@时间复杂度:
*/
func incremovableSubarrayCount(nums []int) int {
	n := len(nums)
	i := 0
	for i < n-1 && nums[i] < nums[i+1] {
		i++
	}
	if n-1 == i {
		return n * (n + 1) / 2
	}

	ans := i + 2
	for j := n - 1; j == n-1 || nums[j] < nums[j+1]; j-- {
		for i >= 0 && nums[i] >= nums[j] {
			i--
		}
		ans += i + 2
	}
	return ans
}
