package main

// 通道1中调用了通道2，通道2中调用通道1,相互等着要对方的数据，造成死锁。
func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go func() {
		for {
			c := <-ch1
			ch2 <- c
		}
	}()

	for {
		c := <-ch2
		ch1 <- c
	}
}
