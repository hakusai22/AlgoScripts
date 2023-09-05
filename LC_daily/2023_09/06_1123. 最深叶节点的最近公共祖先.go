package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/06 00:59
*/

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	_, node := f(root)
	return node
}

func f(root *TreeNode) (int, *TreeNode) {
	if root == nil {
		return 0, nil
	}

	d1, lca1 := f(root.Left)
	d2, lca2 := f(root.Right)
	if d1 > d2 {
		return d1 + 1, lca1
	}
	if d1 < d2 {
		return d2 + 1, lca2
	}
	return d1 + 1, root
}
