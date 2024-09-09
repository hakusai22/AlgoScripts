package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/09 22:38
    @题目     : https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/description/?envType=daily-question&envId=2024-09-01
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func busyStudent(startTime []int, endTime []int, queryTime int) int {
	ans := 0
	for i, x := range startTime {
		if x <= queryTime && queryTime <= endTime[i] {
			ans++
		}
	}
	return ans
}
