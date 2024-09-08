package _14_0908

import (
	"math"
	"slices"
	"sort"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/08 15:55
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func maxPossibleScore(start []int, d int) int {
	slices.Sort(start)
	n := len(start)
	return sort.Search((start[n-1]+d-start[0])/(n-1), func(score int) bool {
		score++
		preX := math.MinInt
		for _, s := range start {
			x := preX + score
			if x > s+d {
				return true
			}
			preX = max(x, s)
		}
		return false
	})
}
