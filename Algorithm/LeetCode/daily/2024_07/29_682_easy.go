package _024_07

import "strconv"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/29 20:22
   @题目     :
   @参考     :
   @时间复杂度:
*/

func calPoints(operations []string) int {
	st := []int{}
	for _, op := range operations {
		switch op[0] {
		case '+':
			st = append(st, st[len(st)-2]+st[len(st)-1])
		case 'D':
			st = append(st, st[len(st)-1]*2)
		case 'C':
			st = st[:len(st)-1]
		default:
			x, _ := strconv.Atoi(op)
			st = append(st, x)
		}
	}
	sum := 0
	for _, x := range st {
		sum += x
	}
	return sum

}
