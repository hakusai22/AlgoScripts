package Sorting

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/14 22:49
*/

func main() {
	var n int
	_, err := fmt.Scanf("%d", &n)
	if err != nil {
		return
	}
	q := make([]int, n)
	for i := 0; i < n; i++ {
		_, err := fmt.Scanf("%d", &q[i])
		if err != nil {
			return
		}
	}
	quickSort(q, 0, n-1)
	for i := 0; i < n; i++ {
		fmt.Printf("%d ", q[i])
	}
	return
}

func quickSort(q []int, l int, r int) {
	if l >= r {
		return
	}
	x := q[l+(r-l)/2]
	i, j := l-1, r+1
	for i < j {
		for {
			i++
			if q[i] >= x {
				break
			}
		}
		for {
			j--
			if q[j] <= x {
				break
			}
		}
		if i < j {
			q[i], q[j] = q[j], q[i]
		}
	}
	quickSort(q, l, j)
	quickSort(q, j+1, r)
}
