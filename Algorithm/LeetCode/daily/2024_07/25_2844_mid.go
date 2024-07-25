package _024_07

import "strings"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/25 19:51
   @题目     :
   @参考     :
   @时间复杂度:
*/

func minimumOperations(num string) int {
	ans := len(num)
	if strings.Contains(num, "0") {
		ans--

	}

	f := func(tail string) {
		i := strings.LastIndexByte(num, tail[1])
		if i <= 0 {
			return
		}
		i = strings.LastIndexByte(num[:i], tail[0])
		if i < 0 {
			return
		}
		ans = min(ans, len(num)-i-2)
	}
	f("00")
	f("25")
	f("50")
	f("75")
	return ans
}
