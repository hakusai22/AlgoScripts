package Bit_Operations

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/10/01 23:30
    @题目     : https://leetcode.cn/problems/number-of-even-and-odd-bits/description/
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func evenOddBit(n int) []int {
	ans := make([]int, 2)
	for i := 0; n > 0; i++ {
		if n&1 == 1 {
			ans[i%2]++
		}
		n >>= 1
	}
	return ans
}
