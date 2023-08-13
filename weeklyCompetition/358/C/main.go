package main

import (
	redblacktree "github.com/emirpasic/gods/trees/redblacktree"
	"math"
	"time"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 12:54
*/

func minAbsoluteDifference(nums []int, x int) int {
	tree := redblacktree.NewWithIntComparator()
	ans := math.MaxInt
	n := len(nums)
	for i := x; i < n; i++ {
		tree.Put(nums[i-x], nums[i-x])
		if v, e := tree.Ceiling(nums[i]); e {
			ans = min(ans, abs(nums[i]-v.Value.(int)))
		}
		if v, e := tree.Floor(nums[i]); e {
			ans = min(ans, abs(nums[i]-v.Value.(int)))
		}
	}
	return ans
}
func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func main() {
	minAbsoluteDifference([]int{4, 3, 2, 4}, 2)
}

/*
红黑树实现
*/
type node struct {
	lr       [2]*node
	priority uint
	key      int
	subCnt   int
}

func (o *node) size() int {
	if o != nil {
		return o.subCnt // 汇总
	}
	return 0
}

func (o *node) maintain() { o.subCnt = 1 + o.lr[0].size() + o.lr[1].size() }

func (o *node) rotate(d int) *node {
	x := o.lr[d^1]
	o.lr[d^1] = x.lr[d]
	x.lr[d] = o
	o.maintain()
	x.maintain()
	return x
}

type treap struct {
	rd   uint
	root *node
}

func (t *treap) fastRand() uint {
	t.rd ^= t.rd << 13
	t.rd ^= t.rd >> 17
	t.rd ^= t.rd << 5
	return t.rd
}

func (t *treap) size() int { return t.root.size() }

func (t *treap) _put(o *node, key int) *node {
	if o == nil {
		return &node{priority: t.fastRand(), key: key, subCnt: 1}
	}
	if d := o.cmp(key); d >= 0 {
		o.lr[d] = t._put(o.lr[d], key)
		if o.lr[d].priority > o.priority {
			o = o.rotate(d ^ 1)
		}
	} else {
		// 相等
	}
	o.maintain()
	return o
}

func (t *treap) put(key int) { t.root = t._put(t.root, key) }

func (t *treap) _delete(o *node, key int) *node {
	if o == nil {
		return nil
	}
	if d := o.cmp(key); d >= 0 {
		o.lr[d] = t._delete(o.lr[d], key)
	} else {
		if o.lr[1] == nil {
			return o.lr[0]
		}
		if o.lr[0] == nil {
			return o.lr[1]
		}
		d = 0
		if o.lr[0].priority > o.lr[1].priority {
			d = 1
		}
		o = o.rotate(d)
		o.lr[d] = t._delete(o.lr[d], key)
	}
	o.maintain()
	return o
}

func (t *treap) delete(key int) { t.root = t._delete(t.root, key) }

func newTreap() *treap { return &treap{rd: uint(time.Now().UnixNano())/2 + 1} }

func (o *node) cmp(a int) int {
	b := o.key
	if a == b {
		return -1
	}
	if a < b {
		return 0
	}
	return 1
}

func (t *treap) min() (min *node) {
	for o := t.root; o != nil; o = o.lr[0] {
		min = o
	}
	return
}

func (t *treap) max() (max *node) {
	for o := t.root; o != nil; o = o.lr[1] {
		max = o
	}
	return
}

func (t *treap) lowerBound(key int) (lb *node) {
	for o := t.root; o != nil; {
		switch c := o.cmp(key); {
		case c == 0:
			lb = o
			o = o.lr[0]
		case c > 0:
			o = o.lr[1]
		default:
			return o
		}
	}
	return // NOTE: check nil
}

func (t *treap) prev(key int) (prev *node) {
	for o := t.root; o != nil; {
		if o.cmp(key) <= 0 {
			o = o.lr[0]
		} else {
			prev = o
			o = o.lr[1]
		}
	}
	return // NOTE: check nil
}
