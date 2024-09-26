package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/26 14:23
    @题目     : https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
    @参考     : https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/solutions/2062785/bian-li-by-endlesscheng-hi82/
    @时间复杂度: O(nlogU)，其中 n 为 nums 的长度，U=max(nums)。
    @空间复杂度:

 数据范围:

*/

func differenceOfSum(nums []int) (ans int) {
	for _, x := range nums {
		ans += x
		for x > 0 {
			ans -= x % 10
			x /= 10
		}
	}
	return ans
}
