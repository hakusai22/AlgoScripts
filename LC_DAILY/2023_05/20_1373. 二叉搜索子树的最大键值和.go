/*
 * @Author: hakusai
 * @Date: 2023-05-20 20:39:08
 * @LastEditTime: 2023-05-20 20:41:09
 * @Description:
 */

package _023_05

import "math"

func maxSumBST(root *TreeNode) (ans int) {
	var dfs func(*TreeNode) (int, int, int)
	dfs = func(node *TreeNode) (int, int, int) {
		if node == nil {
			return math.MaxInt, math.MinInt, 0
		}
		lMin, lMax, lSum := dfs(node.Left)  // 递归左子树
		rMin, rMax, rSum := dfs(node.Right) // 递归右子树
		x := node.Val
		if x <= lMax || x >= rMin { // 不是二叉搜索树
			return math.MinInt, math.MaxInt, 0
		}
		s := lSum + rSum + x // 这棵子树的所有节点值之和
		ans = max(ans, s)
		return min(lMin, x), max(rMax, x), s
	}
	dfs(root)
	return
}
