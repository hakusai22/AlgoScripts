package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/18 08:47
*/

func rob3(root *TreeNode) int {
	return max(dfs(root))
}

func dfs(node *TreeNode) (int, int) {
	if node == nil {
		return 0, 0
	}
	lRob, lNotRob := dfs(node.Left)
	rRob, rNotRob := dfs(node.Right)
	rob := lNotRob + rNotRob + node.Val
	notRob := max(lRob, lNotRob) + max(rRob, rNotRob)
	return rob, notRob
}
