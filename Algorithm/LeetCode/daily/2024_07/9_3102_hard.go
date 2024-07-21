package _024_07

import (
	"github.com/emirpasic/gods/v2/trees/redblacktree"
	"math"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/21 12:03
   @题目     : https://leetcode.cn/problems/minimize-manhattan-distances/description/?envType=daily-question&envId=2024-07-09
   @参考     : https://leetcode.cn/problems/minimize-manhattan-distances/solutions/2835856/python3javacgotypescript-yi-ti-yi-jie-yo-e76n/?envType=daily-question&envId=2024-07-09
   @时间复杂度:
*/

func minimumDistance(points [][]int) int {
	st1 := redblacktree.New[int, int]()
	st2 := redblacktree.New[int, int]()
	merge := func(st *redblacktree.Tree[int, int], x, v int) {
		c, _ := st.Get(x)
		if c+v == 0 {
			st.Remove(x)
		} else {
			st.Put(x, c+v)
		}
	}
	for _, p := range points {
		x, y := p[0], p[1]
		merge(st1, x+y, 1)
		merge(st2, x-y, 1)
	}
	ans := math.MaxInt
	for _, p := range points {
		x, y := p[0], p[1]
		merge(st1, x+y, -1)
		merge(st2, x-y, -1)
		ans = min(ans, max(st1.Right().Key-st1.Left().Key, st2.Right().Key-st2.Left().Key))
		merge(st1, x+y, 1)
		merge(st2, x-y, 1)
	}
	return ans
}
