package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/09 22:41
    @题目     : https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/description/?envType=daily-question&envId=2024-09-02
    @参考     : https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/?envType=daily-question&envId=2024-09-02
    @时间复杂度: O(n)
    @空间复杂度:

 数据范围:

*/

func maxConsecutiveAnswers(answerKey string, k int) int {
	cnt := [2]int{}
	left := 0
	ans := 0
	for right, ch := range answerKey {
		cnt[ch>>1&1]++
		for cnt[0] > k && cnt[1] > k {
			cnt[answerKey[left]>>1&1]--
			left++
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
