package main

import (
	"strconv"
)

func countSymmetricIntegers(low int, high int) (ans int) {
	for i := low; i <= high; i++ {
		s := strconv.Itoa(i)
		n := len(s)
		if n%2 > 0 {
			continue
		}
		sum := 0
		for _, c := range s[:n/2] {
			sum += int(c)
		}
		for _, c := range s[n/2:] {
			sum -= int(c)
		}
		if sum == 0 {
			ans++
		}
	}
	return
}
