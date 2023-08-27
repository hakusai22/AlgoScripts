package main

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/27 10:28
*/

func furthestDistanceFromOrigin(moves string) int {
	countL := 0
	countR := 0
	countUnderscore := 0

	for _, move := range moves {
		switch move {
		case 'L':
			countL++
		case 'R':
			countR++
		case '_':
			countUnderscore++
		}
	}
	return abs(countL-countR) + countUnderscore
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
