package Segment_Tree

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/10 16:20
*/

type pair struct{ first, second int }
type MyCalendarTwo map[int]pair

//func Constructor() MyCalendarTwo {
//	return MyCalendarTwo{}
//}

func (tree MyCalendarTwo) update(start, end, val, l, r, idx int) {
	if r < start || end < l {
		return
	}
	if start <= l && r <= end {
		p := tree[idx]
		p.first += val
		p.second += val
		tree[idx] = p
		return
	}
	mid := (l + r) >> 1
	tree.update(start, end, val, l, mid, 2*idx)
	tree.update(start, end, val, mid+1, r, 2*idx+1)
	p := tree[idx]
	p.first = p.second + max(tree[2*idx].first, tree[2*idx+1].first)
	tree[idx] = p
}

func (tree MyCalendarTwo) Book(start, end int) bool {
	tree.update(start, end-1, 1, 0, 1e9, 1)
	if tree[1].first > 2 {
		tree.update(start, end-1, -1, 0, 1e9, 1)
		return false
	}
	return true
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
