package _38

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/03 14:41
*/

func primeSubOperation(a []int) (ans bool) {

	const mx int = 2000
	primes := []int{}
	isP := [mx + 1]bool{}
	for i := range isP {
		isP[i] = true
	}
	isP[0], isP[1] = false, false
	for i := 2; i <= mx; i++ {
		if isP[i] {
			primes = append(primes, i)
			for j := i * i; j <= mx; j += i {
				isP[j] = false
			}
		}
	}

	pre := -int(1e9)
	for i, v := range a {
		for _, p := range primes {
			if v <= p {
				break
			}
			if v-p > pre {
				a[i] = v - p
			} else {
				break
			}
		}
		pre = a[i]
	}

	for i := 1; i < len(a); i++ {
		if a[i] <= a[i-1] {
			return
		}
	}
	return true
}
