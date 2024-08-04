package ants

import (
	"fmt"
	"github.com/panjf2000/ants/v2"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 18:42
*/

var num int32

func addNum(i int32) {
	atomic.AddInt32(&num, i)
	time.Sleep(time.Millisecond)
	fmt.Println("now num =", num)
}

/*
*
使用Ants
running goroutines: 3230
num = 10000

	--- PASS: TestAnt (0.10s)

PASS
*/
func TestAnt(t *testing.T) {
	defer ants.Release()

	var wg sync.WaitGroup
	syncCalculateSum := func() {
		addNum(1)
		wg.Done()
	}

	runTimes := 10000

	for i := 0; i < runTimes; i++ {
		wg.Add(1)
		_ = ants.Submit(syncCalculateSum) //需要执行的方法
	}

	wg.Wait()

	fmt.Printf("running goroutines: %d\n", ants.Running())
	fmt.Printf("num = %d \n ", num)
}

/*
*
使用Ants控制协程数量
running goroutines: 100
num = 10000

	--- PASS: TestAntPool (0.11s)

PASS
*/
func TestAntPool(t *testing.T) {
	defer ants.Release()

	var wg sync.WaitGroup
	f := func() {
		addNum(1)
		wg.Done()
	}
	runTimes := 10000
	pool, _ := ants.NewPool(100)

	for i := 0; i < runTimes; i++ {
		wg.Add(1)
		_ = pool.Submit(f)
	}
	wg.Wait()

	fmt.Printf("running goroutines: %d\n", pool.Running())
	fmt.Printf("num = %d \n ", num)
}

/*
*
Ants还支持另一种形式，执行具体的函数：
*/
func TestAntWithFunc(t *testing.T) {
	defer ants.Release()

	runTimes := 10000

	var wg sync.WaitGroup

	p, _ := ants.NewPoolWithFunc(10, func(i interface{}) {
		addNum(i.(int32))
		wg.Done()
	})
	defer p.Release()

	for i := 0; i < runTimes; i++ {
		wg.Add(1)
		_ = p.Invoke(int32(1)) //这个地方参数可以传结构体
	}
	wg.Wait()
	fmt.Printf("running goroutines: %d\n", p.Running())
	fmt.Printf("finish all tasks, result is %d\n", num)
}

/*
*
Ants还提供了NewMultiPool类，初始化多个协程池
*/
func TestMultiPool(t *testing.T) {
	defer ants.Release()

	runTimes := 10000

	var wg sync.WaitGroup

	f := func() {
		addNum(1)
		wg.Done()
	}

	//10表示初始化10个协程池，-1位置参数表示协程池的容量，值为-1时代表不限制容量
	mp, _ := ants.NewMultiPool(10, -1, ants.RoundRobin)
	defer func() {
		_ = mp.ReleaseTimeout(5 * time.Second)
	}()
	for i := 0; i < runTimes; i++ {
		wg.Add(1)
		_ = mp.Submit(f)
	}

	wg.Wait()
	fmt.Printf("running goroutines: %d\n", mp.Running())
	fmt.Printf("finish all tasks, result is %d\n", num)
}
