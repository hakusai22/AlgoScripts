package _023_09

import (
	"container/heap"
	"sort"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/11 08:20
*/
func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})
	T := 0
	var maxHeap = maxHeap_{}
	for _, cours := range courses {
		cost, deapline := cours[0], cours[1]
		T += cost
		heap.Push(&maxHeap, cost)
		if T > deapline {
			T -= maxHeap.IntSlice[0]
			heap.Pop(&maxHeap)
		}
	}
	return maxHeap.Len()
}

//------------- 自定义最大堆 ------------------//
type maxHeap_ struct {
	sort.IntSlice
}

//----比较函数
func (h maxHeap_) Less(i int, j int) bool {
	return h.IntSlice[i] > h.IntSlice[j]
}

//----Push操作
func (h *maxHeap_) Push(v interface{}) {
	h.IntSlice = append(h.IntSlice, v.(int))
}

//----Pop()操作
func (h *maxHeap_) Pop() (_ interface{}) {
	a := h.IntSlice
	x := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return x
}
