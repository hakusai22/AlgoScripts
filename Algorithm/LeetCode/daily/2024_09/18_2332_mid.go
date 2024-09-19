package _024_09

import "sort"

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/19 22:53
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
	sort.Ints(buses)
	sort.Ints(passengers)
	j, c := 0, 0
	for _, t := range buses {
		c = capacity
		for c > 0 && j < len(passengers) && passengers[j] <= t {
			j++
			c--
		}
	}
	j--
	ans := buses[len(buses)-1]
	if c == 0 {
		ans = passengers[j]
	}
	for j >= 0 && ans == passengers[j] {
		ans--
		j--
	}
	return ans
}
