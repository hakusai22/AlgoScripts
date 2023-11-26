package _70_3

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/20 22:21
*/
func maximumScoreAfterOperations(edges [][]int, values []int) int64 {
	g := make([][]int, len(values))
	g[0] = append(g[0], -1) // 避免误把根节点当作叶子
	for _, e := range edges {
		x, y := e[0], e[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}

	total := 0
	// dfs(x, fa) 计算以 x 为根的子树是健康时，失去的最小分数
	var dfs func(int, int) int
	dfs = func(x, fa int) int {
		total += values[x]
		if len(g[x]) == 1 { // x 是叶子
			return values[x]
		}
		loss := 0 // 第二种情况
		for _, y := range g[x] {
			if y != fa {
				loss += dfs(y, x) // 计算以 y 为根的子树是健康时，失去的最小分数
			}
		}
		return min(values[x], loss) // 两种情况取最小值
	}
	return int64(total - dfs(0, -1))
}

func min(i int, loss int) int {
	if i > loss {
		return loss
	} else {
		return i
	}
}
