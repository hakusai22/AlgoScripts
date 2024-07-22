package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/22 18:04
   @题目     : https://leetcode.cn/problems/detonate-the-maximum-bombs/description/?envType=daily-question&envId=2024-07-22
   @参考     : https://leetcode.cn/problems/detonate-the-maximum-bombs/?envType=daily-question&envId=2024-07-22
   @时间复杂度:
*/

func maximumDetonation(bombs [][]int) int {
	n := len(bombs)
	g := make([][]int, n)
	for i, p := range bombs {
		x, y, r := p[0], p[1], p[2]
		for j, q := range bombs {
			dx := x - q[0]
			dy := y - q[1]
			if j != i && dx*dx+dy*dy <= r*r {
				g[i] = append(g[i], j)
			}
		}
	}
	vis := make([]bool, n)
	var dfs func(int) int
	dfs = func(x int) int {
		vis[x] = true
		cnt := 1
		for _, y := range g[x] {
			if !vis[y] {
				cnt += dfs(y)
			}
		}
		return cnt
	}

	ans := 0
	for i := range g {
		clear(vis)
		ans = max(ans, dfs(i))
	}
	return ans
}
