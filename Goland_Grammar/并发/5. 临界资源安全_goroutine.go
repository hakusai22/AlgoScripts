/*
 * @Author: hakusai
 * @Date: 2023-04-16 23:06:21
 * @LastEditTime: 2023-05-19 14:42:07
 * @Description:
 */
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 定义全局变量 表示救济粮食总量
var food = 10

func main() {
	//开启4个协程抢粮食
	go Relief("灾民好家伙1")
	go Relief("灾民好家伙2")
	go Relief("灾民老李头1")
	go Relief("灾民老李头2")

	//让程序休息5秒等待所有子协程执行完毕
	time.Sleep(5 * time.Second)
}

// 定义一个发放的方法
func Relief(name string) {
	for {
		if food > 0 { //此时有可能第二个goroutine访问的时候 第一个goroutine还未执行完 所以条件也成立
			time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond) //随机休眠时间
			food--
			fmt.Println(name, "抢到救济粮 ，还剩下", food, "个")
		} else {
			fmt.Println(name, "别抢了 没有粮食了。")
			break
		}
	}
}

//结果
//灾民好家伙1 抢到救济粮 ，还剩下 8 个
//灾民老李头1 抢到救济粮 ，还剩下 7 个
//灾民好家伙1 抢到救济粮 ，还剩下 6 个
//灾民老李头1 抢到救济粮 ，还剩下 5 个
//灾民老李头2 抢到救济粮 ，还剩下 4 个
//灾民好家伙2 抢到救济粮 ，还剩下 3 个
//灾民好家伙1 抢到救济粮 ，还剩下 2 个
//灾民老李头1 抢到救济粮 ，还剩下 1 个
//灾民老李头2 抢到救济粮 ，还剩下 0 个
//灾民老李头2 别抢了 没有粮食了。
//灾民老李头1 抢到救济粮 ，还剩下 -1 个
//灾民老李头1 别抢了 没有粮食了。
//灾民好家伙1 抢到救济粮 ，还剩下 -2 个
//灾民好家伙1 别抢了 没有粮食了。
//灾民好家伙2 抢到救济粮 ，还剩下 -3 个
//灾民好家伙2 别抢了 没有粮食了。
