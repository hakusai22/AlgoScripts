package _95_0505

import (
	"fmt"
	"testing"
)

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2024/05/05 00:58
*/

func TestMinEnd(t *testing.T) {
	end := minEnd(2, 7)
	fmt.Println(end)
}

func minEnd(n int, x int) int64 {
	n--
	i, j := 0, 0
	for n>>j > 0 {
		if x>>i&1 == 0 {
			bit := n >> j & 1
			x |= bit << i
			j++
		}
		i++
	}
	return int64(x)
}
