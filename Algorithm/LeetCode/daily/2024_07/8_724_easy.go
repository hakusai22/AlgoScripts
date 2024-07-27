package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/27 22:16
   @题目     :
   @参考     :
   @时间复杂度:
*/

func pivotIndex(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	leftS := 0
	for i, x := range nums {
		if leftS*2 == s-x {
			return i
		}
		leftS += x
	}
	return -1
}
