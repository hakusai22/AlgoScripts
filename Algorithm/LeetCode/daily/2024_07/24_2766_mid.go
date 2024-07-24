package _024_07

import "slices"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/24 23:17
   @题目     :
   @参考     :
   @时间复杂度:
*/

func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {

	set := map[int]struct{}{}
	for _, x := range nums {
		set[x] = struct{}{}
	}

	for i, x := range moveFrom {
		delete(set, x)
		set[moveTo[i]] = struct{}{}
	}

	ans := make([]int, 0, len(set))
	for x := range set {
		ans = append(ans, x)
	}
	slices.Sort(ans)
	return ans

}
