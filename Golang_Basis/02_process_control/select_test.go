package _2_process_control

import (
	"fmt"
	"testing"
	"time"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 02:05
   @题目     :
   @参考     :
   @时间复杂度:
*/

// select 语句类似于 switch 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。

func TestSelect(t *testing.T) {
	var c1, c2, c3 chan int
	var i1, i2 int
	select {
	case i1 = <-c1:
		fmt.Println("received ", i1, " from c1")
	case c2 <- i2:
		fmt.Println("sent ", i2, " to c2")
	case i3, ok := (<-c3): // same as: i3, ok := <-c3
		if ok {
			fmt.Println("received ", i3, " from c3")
		} else {
			fmt.Println("c3 is closed")
		}
	default:
		fmt.Printf("no communication")
	}

	//在某些情况下是存在不希望channel缓存满了的需求的，可以用如下方法判断
	ch := make(chan int, 5)
	//...
	data := 0
	select {
	case ch <- data:
	default:
		//做相应操作，比如丢弃data。视需求而定
	}
}

// 比如在下面的场景中，使用全局resChan来接受response，如果时间超过3S,resChan中还没有数据返回，则第二条case将执行
var resChan = make(chan int)

func test() {
	select {
	case data := <-resChan:
		doData(data)
	case <-time.After(time.Second * 3):
		fmt.Println("request time out")
	}
}

func doData(data int) {
	//...
}
