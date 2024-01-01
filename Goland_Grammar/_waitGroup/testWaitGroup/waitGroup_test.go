package main

import (
	"sync"
	"testing"
	"time"
)

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/01/01 19:25
*/

func Test_waitGroup(t *testing.T) {
	tasksNum := 10

	dataCh := make(chan interface{})
	// 启动写 goroutine，推进并发获取数据进程，将获取到的数据聚合到 channel 中
	go func() {
		// 保证获取到所有数据后，通过 channel 传递到读协程手中
		var wg sync.WaitGroup
		for i := 0; i < tasksNum; i++ {
			wg.Add(1)
			go func(ch chan<- interface{}) {
				defer wg.Done()
				ch <- time.Now().UnixNano()
			}(dataCh)
		}
		// 确保所有取数据的协程都完成了工作，才关闭 ch
		wg.Wait()
		close(dataCh)
	}()

	resp := make([]interface{}, 0, tasksNum)
	// 主协程作为读协程，持续读取数据，直到所有写协程完成任务，chan 被关闭后才会往下
	for data := range dataCh {
		resp = append(resp, data)
	}
	t.Logf("resp: %+v", resp)
}

func TestAdd(t *testing.T) {
	if ans := Add(1, 2); ans != 3 {
		t.Errorf("1 + 2 expected be 3, but %d got", ans)
	}

	if ans := Add(-10, -20); ans != -30 {
		t.Errorf("-10 + -20 expected be -30, but %d got", ans)
	}
}

func Add(a int, b int) int {
	return a + b
}

func Mul(a int, b int) int {
	return a * b
}
