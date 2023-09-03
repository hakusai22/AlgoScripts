package main

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 12:57
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	current := head

	for current != nil {
		next := current.Next
		current.Next = prev
		prev = current
		current = next
	}

	return prev
}

func doubleIt(head *ListNode) *ListNode {
	// 先将链表翻转
	reversed := reverseList(head)

	// 对翻转后的链表进行翻倍操作
	carry := 0
	current := reversed
	dummy := &ListNode{}
	tail := dummy

	for current != nil {
		newVal := current.Val*2 + carry
		carry = newVal / 10
		tail.Next = &ListNode{Val: newVal % 10}
		tail = tail.Next
		current = current.Next
	}

	// 处理最后的进位
	for carry > 0 {
		tail.Next = &ListNode{Val: carry % 10}
		tail = tail.Next
		carry /= 10
	}

	// 最后将链表再次翻转回来
	return reverseList(dummy.Next)
}
