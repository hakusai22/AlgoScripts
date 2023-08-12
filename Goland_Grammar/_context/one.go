/*
 * @Author: hakusai
 * @Date: 2023-05-17 23:15:58
 * @LastEditTime: 2023-05-17 23:32:23
 * @Description:
 */
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())

	go Worker(ctx, "node-1")
	go Worker(ctx, "node-2")
	go Worker(ctx, "node-3")

	time.Sleep(time.Second * 5)

	fmt.Println("stop worker")
	cancel()

	time.Sleep(time.Second * 3)
}

func Worker(ctx context.Context, name string) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println(name + " done!")
			return
		default:
			fmt.Println(name + " ing...")
			time.Sleep(time.Second)
		}
	}
}
