package Segment_Tree

import "github.com/emirpasic/gods/trees/redblacktree"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/10 14:32
*/

type MyCalendar struct {
	*redblacktree.Tree
}

func Constructor() MyCalendar {
	t := redblacktree.NewWithIntComparator()
	t.Put(-1, -1)
	return MyCalendar{
		t,
	}
}

func (c *MyCalendar) Book(start int, end int) bool {
	floor, _ := c.Floor(start)
	if floor.Value.(int) > start {
		return false
	}
	if it := c.IteratorAt(floor); it.Next() && it.Key().(int) < end {
		return false
	}
	c.Put(start, end)
	return true
}
