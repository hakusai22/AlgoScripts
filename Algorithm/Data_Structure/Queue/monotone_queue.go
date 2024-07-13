package Queue

/*
	单调队列 Monotone Queue
	需要不断维护队列的单调性，时刻保证队列元素从大到小或从小到大
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/09 23:17
*/

type MqData struct {
	Val int
	Del int // 懒删除标记
}

type MonotoneQueue struct {
	Data []MqData
	Size int // 单调队列对应的区间的长度
}

func (mq MonotoneQueue) Less(a, b MqData) bool {
	return a.Val >= b.Val // >= 维护区间最大值；<= 维护区间最小值
}

func (mq *MonotoneQueue) Push(v int) {
	mq.Size++
	d := MqData{v, 1}
	for len(mq.Data) > 0 && mq.Less(d, mq.Data[len(mq.Data)-1]) {
		d.Del += mq.Data[len(mq.Data)-1].Del
		mq.Data = mq.Data[:len(mq.Data)-1]
	}
	mq.Data = append(mq.Data, d)
}

func (mq *MonotoneQueue) Pop() {
	mq.Size--
	if mq.Data[0].Del > 1 {
		mq.Data[0].Del--
	} else {
		mq.Data = mq.Data[1:]
	}
}

// 返回区间最值
// 调用前需保证 mq.size > 0
func (mq MonotoneQueue) Top() int {
	return mq.Data[0].Val
}
