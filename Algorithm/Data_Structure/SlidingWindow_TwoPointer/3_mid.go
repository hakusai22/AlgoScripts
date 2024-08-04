package SlidingWindow_TwoPointer

/*
@Author  : https://github.com/hakusai22
@Time    : 2024/08/04 15:26
@题目     : https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
@参考     : https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/1959540/xia-biao-zong-suan-cuo-qing-kan-zhe-by-e-iaks/
@时间复杂度: O(n)，其中 n 为 s 的长度。注意 left 至多增加 n 次，所以整个二重循环至多循环 O(n) 次。
@空间复杂度: O(∣Σ∣)，其中 ∣Σ∣ 为字符集合的大小，本题中字符均为 ASCII 字符，所以 ∣Σ∣≤128。
*/
func lengthOfLongestSubstring(s string) int {
	ans, left := 0, 0
	window := [128]bool{}
	for right, c := range s {
		for window[c] {
			window[s[left]] = false
			left++
		}
		window[c] = true
		ans = max(ans, right-left+1)
	}
	return ans
}
