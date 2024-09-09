package _024_09

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/09 08:53
    @题目     : https://leetcode.cn/problems/merge-nodes-in-between-zeros/description/
    @参考     : https://leetcode.cn/problems/merge-nodes-in-between-zeros/solutions/1278727/jian-ji-xie-fa-by-endlesscheng-c4gf/
    @时间复杂度: O(n)，其中 n 是链表长度
    @空间复杂度: O(1)。没有创建新的节点

 数据范围:

*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeNodes(head *ListNode) *ListNode {
	tail := head
	for cur := head.Next; cur.Next != nil; cur = cur.Next {
		if cur.Val != 0 {
			tail.Val += cur.Val
		} else {
			tail = tail.Next
			tail.Val = 0
		}
	}
	tail.Next = nil
	return head
}
