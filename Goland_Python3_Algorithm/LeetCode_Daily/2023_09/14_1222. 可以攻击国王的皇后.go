package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/14 08:49
*/

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	q := make(map[int]bool)
	for _, queen := range queens {
		q[queen[0]*8+queen[1]] = true
	}
	var ans [][]int
	for _, dx := range []int{-1, 0, 1} {
		for _, dy := range []int{-1, 0, 1} {
			if dx == 0 && dy == 0 {
				continue
			}
			kx, ky := king[0]+dx, king[1]+dy
			for kx >= 0 && kx < 8 && ky >= 0 && ky < 8 {
				if q[kx*8+ky] {
					ans = append(ans, []int{kx, ky})
					break
				}
				kx += dx
				ky += dy
			}
		}
	}
	return ans
}
