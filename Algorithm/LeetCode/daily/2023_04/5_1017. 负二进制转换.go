package _023_04

/*
-*- coding: utf-8 -*-
@Author  : wheat
@Time    : 2023/04/06 08:23
*/
func baseNeg2(n int) string {
	if n == 0 {
		return "0"
	}
	const BASE = -2
	var ans []byte
	for n != 1 {
		if n > 0 {
			ans = append(ans, byte('0'+n%BASE))
			n /= BASE
		} else {
			yu := n % BASE
			if yu == -1 {
				n = n/BASE + 1
				ans = append(ans, '0'+byte(1))
			} else {
				ans = append(ans, '0'+byte(yu))
				n /= BASE
			}
		}
	}
	ans = append(ans, '0'+byte(1))
	length := len(ans)
	//反转
	for i := 0; i < length/2; i++ {
		ans[i], ans[length-1-i] = ans[length-1-i], ans[i]
	}
	return string(ans)
}
