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

func doubleIt(head *ListNode) *ListNode {
	c := f(head)
	if c == 1 {
		return &ListNode{Val: 1, Next: head}
	}
	return head
}
func f(head *ListNode) int {
	if head == nil {
		return 0
	}
	c := f(head.Next)
	head.Val = 2*head.Val + c
	head.Val, c = head.Val%10, head.Val/10
	return c
}
