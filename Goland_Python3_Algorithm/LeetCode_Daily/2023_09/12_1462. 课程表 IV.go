package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/12 23:43
*/

func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {

	f := make([][]bool, numCourses)
	for i := range f {
		f[i] = make([]bool, numCourses)
	}
	for _, prerequisite := range prerequisites {
		f[prerequisite[0]][prerequisite[1]] = true
	}
	for i := 0; i < numCourses; i++ {
		for j := 0; j < numCourses; j++ {
			for k := 0; k < numCourses; k++ {
				if f[j][i] && f[i][k] {
					f[j][k] = true
				}
			}
		}
	}
	var ans []bool
	for _, query := range queries {
		ans = append(ans, f[query[0]][query[1]])
	}
	return ans
}
