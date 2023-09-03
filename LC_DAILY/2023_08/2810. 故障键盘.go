/*
 * @Author: hakusai
 * @Date: 2023-08-10 02:30:25
 * @LastEditTime: 2023-08-10 02:33:31
 * @Description: https://github.com/hakusai22
 */
package main

func finalString(s string) (ans string) {
	a := []rune{}
	for _, v := range s {
		if v == 'i' {
			for i, n := 0, len(a); i < n/2; i++ {
				a[i], a[n-i-1] = a[n-1-i], a[i]
			}
		} else {
			a = append(a, v)
		}
	}
	ans = string(a)
	return
}
