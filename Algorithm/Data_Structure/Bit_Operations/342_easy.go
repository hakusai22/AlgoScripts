package Bit_Operations

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/10/01 23:49
    @题目     : https://leetcode.cn/problems/power-of-four/description/
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func isPowerOfFour(n int) bool {
	return n > 0 && n&(n-1) == 0 && n%3 == 1
}
