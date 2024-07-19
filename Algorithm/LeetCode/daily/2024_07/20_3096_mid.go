package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/19 14:53
   @题目     :
   @参考     :
   @时间复杂度:
*/

func minimumLevels(possible []int) int {
	s := 0
	for _, x := range possible {
		if x == 0 {
			s += -1
		} else {
			s++
		}
	}
	t := 0
	for i, x := range possible[:len(possible)-1] {
		if x == 0 {
			t += -1
		} else {
			t++
		}
		if t > s-t {
			return i + 1
		}
	}
	return -1
}
