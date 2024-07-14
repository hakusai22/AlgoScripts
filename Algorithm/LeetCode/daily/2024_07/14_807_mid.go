package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/14 21:49
   @题目     : https://leetcode.cn/problems/max-increase-to-keep-city-skyline/description/?envType=daily-question&envId=2024-07-14
   @参考     : https://leetcode.cn/problems/max-increase-to-keep-city-skyline/solutions/2842679/zeng-jia-dao-xing-lie-zui-da-zhi-pythonj-bvb8/?envType=daily-question&envId=2024-07-14
   @时间复杂度: 时间复杂度：O(mn)，其中 m 和 n 分别为 grid 的行数和列数。
*/

func maxIncreaseKeepingSkyline(grid [][]int) int {
	rowMax := make([]int, len(grid))
	colMax := make([]int, len(grid[0]))
	ans := 0
	for i, row := range grid {
		for j, x := range row {
			rowMax[i] = max(rowMax[i], x)
			colMax[j] = max(colMax[j], x)
		}
	}
	for i, ints := range grid {
		for j, x := range ints {
			ans += min(rowMax[i], colMax[j]) - x
		}
	}
	return ans
}
