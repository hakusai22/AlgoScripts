package main

import (
	"fmt"
)

func main() {
	c := make(chan int)

	go func() {
		for i := 0; i < 5; i++ {
			c <- i
		}
		close(c)
	}()

	for {
		//ok为true说明channel没有关闭，为false说明管道已经关闭
		if data, ok := <-c; ok {
			fmt.Println(data)
		} else {
			break
		}
	}

	fmt.Println("Finished")

	c1 := make(chan int)

	go func() {
		for i := 0; i < 5; i++ {
			c1 <- i
		}
	}()

	for data := range c {
		fmt.Println(data)
	}
	fmt.Println("Finished")
}
