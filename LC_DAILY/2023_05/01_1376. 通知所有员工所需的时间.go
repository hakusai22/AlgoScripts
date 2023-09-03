/*
 * @Author: hakusai
 * @Date: 2023-05-21 19:49:46
 * @LastEditTime: 2023-05-21 19:57:18
 * @Description:
 */

package _023_05

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	g := make([][]int, n)
	for i, x := range manager {
		if x != -1 {
			g[x] = append(g[x], i)
		}
	}
	var dfs func(int) int
	dfs = func(i int) (ans int) {
		for _, j := range g[i] {
			ans = max(ans, dfs(j)+informTime[i])
		}
		return
	}
	return dfs(headID)
}
