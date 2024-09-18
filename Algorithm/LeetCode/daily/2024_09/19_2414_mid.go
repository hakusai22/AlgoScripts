package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/19 01:08
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func longestContinuousSubstring(s string) int {
	ans, cnt := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i-1]+1 == s[i] {
			cnt++
			ans = max(ans, cnt)
		} else {
			cnt = 1
		}
	}
	return ans
}
