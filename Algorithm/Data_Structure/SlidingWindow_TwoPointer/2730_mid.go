package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 16:06
    @题目     : https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/
    @参考     : https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/solutions/2304713/shuang-zhi-zhen-hua-chuang-pythonjavacgo-nurf/
    @时间复杂度: O(n)，其中 n 为 s 的长度。注意 left 只会增加不会减少，所以二重循环的时间复杂度为 O(n)。
    @空间复杂度: O(1)。仅用到若干额外变量。

 数据范围:
1 <= s.length <= 50
'0' <= s[i] <= '9'
*/

func longestSemiRepetitiveSubstring(s string) int {
	ans, left, same := 1, 0, 0
	for right := 1; right < len(s); right++ {
		if s[right] == s[right-1] {
			same++
			if same > 1 {
				left++
				for s[left] != s[left-1] {
					left++
				}
				same = 1
			}
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
