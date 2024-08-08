package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/08 10:17
    @题目     : https://leetcode.cn/problems/minimum-window-substring/description/
    @参考     : https://leetcode.cn/problems/minimum-window-substring/solutions/2713911/liang-chong-fang-fa-cong-o52mn-dao-omnfu-3ezz/
    @时间复杂度: O(∣Σ∣m+n)，其中 m 为 s 的长度，n 为 t 的长度，∣Σ∣ 为字符集合的大小，本题字符均为英文字母，所以 ∣Σ∣=52。注意 left 只会增加不会减少，left 每增加一次，我们就花费 O(∣Σ∣) 的时间。因为 left 至多增加 m 次，所以二重循环的时间复杂度为 O(∣Σ∣m)，再算上统计 t 字母出现次数的时间 O(n)，总的时间复杂度为 O(∣Σ∣m+n)。
    @空间复杂度: O(∣Σ∣)。如果创建了大小为 128 的数组，则 ∣Σ∣=128。

 数据范围:
m == s.length
n == t.length
1 <= m, n <= 10^5
s 和 t 由英文字母组成
*/

func minWindow(s string, t string) string {
	m := len(s)
	l, r, left := -1, m, 0
	var cntS, cntT [128]int
	for _, c := range t {
		cntT[c]++
	}

	for right, c := range s {
		cntS[c]++
		for isCovered(cntS[:], cntT[:]) {
			if right-left < r-l {
				l, r = left, right
			}
			// 覆盖 缩小范围
			cntS[s[left]]--
			left++
		}
	}
	if l < 0 {
		return ""
	}
	return s[l : r+1]
}

func isCovered(cntS, cntT []int) bool {
	for i := 'A'; i <= 'Z'; i++ {
		if cntS[i] < cntT[i] {
			return false
		}
	}
	for i := 'a'; i <= 'z'; i++ {
		if cntS[i] < cntT[i] {
			return false
		}
	}
	return true
}
