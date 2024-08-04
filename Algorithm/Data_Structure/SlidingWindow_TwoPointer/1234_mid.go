package SlidingWindow_TwoPointer

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 19:49
    @题目     : https://leetcode.cn/problems/replace-the-substring-for-balanced-string/description/
    @参考     : https://leetcode.cn/problems/replace-the-substring-for-balanced-string/solutions/2108358/tong-xiang-shuang-zhi-zhen-hua-dong-chua-z7tu/
    @时间复杂度: O(nC)，其中 n 为 s 的长度，C=4。
    @空间复杂度: O(C)。如果用哈希表实现，可以做到 O(C)。

 数据范围:
提示：
1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符
*/

// 设子串的左右端点为 left 和 right，枚举 right，如果子串外的任意字符的出现次数都不超过 m，
//则说明从 left 到 right 的这段子串可以是待替换子串，用其长度 right−left+1 更新答案的最小值，
//并向右移动 left，缩小子串长度。

func balancedString(s string) int {
	cnt, m := ['X']int{}, len(s)/4
	for _, c := range s {
		cnt[c]++
	}
	if cnt['Q'] == m && cnt['W'] == m && cnt['E'] == m && cnt['R'] == m {
		return 0
	}
	ans, left := len(s), 0
	for right, c := range s {
		cnt[c]--
		for cnt['Q'] <= m && cnt['W'] <= m && cnt['E'] <= m && cnt['R'] <= m {
			ans = min(ans, right-left+1)
			cnt[s[left]]++
			left++
		}
	}
	return ans
}
