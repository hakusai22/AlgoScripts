package Bit_Operations

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/10/01 15:39
    @题目     : https://leetcode.cn/problems/xor-operation-in-an-array/
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func xorOperation(n int, start int) int {
	ans := start
	for i := 1; i < n; i++ {
		ans ^= start + 2*i
	}
	return ans
}
