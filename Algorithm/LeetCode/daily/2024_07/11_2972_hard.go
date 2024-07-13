package _024_07

/*
@Author  : https://github.com/hakusai22
@Time    : 2024/07/13 17:57
@题目     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/description/?envType=daily-question&envId=2024-07-11
@参考     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/solutions/2577663/shuang-zhi-zhen-on-shi-jian-o1-kong-jian-2hsz/?envType=daily-question&envId=2024-07-11
@时间复杂度: 时间复杂度：O(n)，其中 n 为 nums 的长度。注意二重循环中的下标 i 和 j 都只会减小，不会变大。由于下标只会减小 O(n) 次，所以二重循环的总循环次数是 O(n) 的。
*/

func incremovableSubarrayCount_2972(nums []int) int64 {
	n := len(nums)
	i := 0
	for i < n-1 && nums[i] < nums[i+1] {
		i++
	}
	if n-1 == i {
		return int64(n) * int64(n+1) / 2
	}

	ans := int64(i + 2)
	for j := n - 1; j == n-1 || nums[j] < nums[j+1]; j-- {
		for i >= 0 && nums[i] >= nums[j] {
			i--
		}
		ans += int64(i + 2)
	}
	return ans
}
