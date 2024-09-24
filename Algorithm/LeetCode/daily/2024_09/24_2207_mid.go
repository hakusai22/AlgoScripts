package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/24 15:43
    @题目     : https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/description/?envType=daily-question&envId=2024-09-24
    @参考     : https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/?envType=daily-question&envId=2024-09-24
    @时间复杂度: O(n)
    @空间复杂度:

 数据范围:

*/

func maximumSubsequenceCount(text string, pattern string) int64 {
	ans := 0
	x, y := 0, 0
	for _, c := range text {
		if byte(c) == pattern[1] {
			y++
			ans += x
		}
		if byte(c) == pattern[0] {
			x++
		}
	}
	return int64(ans) + int64(max(x, y))
}
