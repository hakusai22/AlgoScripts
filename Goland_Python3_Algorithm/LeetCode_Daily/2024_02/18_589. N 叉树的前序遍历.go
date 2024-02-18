package _024_02

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/02/18 23:42
*/

type Node struct {
	Val      int
	Children []*Node
}

func preorder(root *Node) (ans []int) {
	var dfs func(*Node)
	dfs = func(node *Node) {
		if node == nil {
			return
		}
		ans = append(ans, node.Val)
		for _, c := range node.Children {
			dfs(c)
		}
	}
	dfs(root)
	return
}
