# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 21:17
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表
        head = tree = ListNode()

        val = tmp = 0
        # 当三者有一个不为空时继续循环
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next
