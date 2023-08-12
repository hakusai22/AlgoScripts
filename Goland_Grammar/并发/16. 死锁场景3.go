package main

// 协程开启之前就放数据,还没有准备好，就放数据，就会造成死锁。
func main() {
	c := make(chan int)
	c <- 88
	go func() {
		<-c
	}()
}
