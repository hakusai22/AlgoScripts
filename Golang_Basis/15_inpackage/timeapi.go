package main

import (
	"fmt"
	"time"
)

// 时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总毫秒数。它主要是为用户提供一份电子证据.
func main() {
	//获取指定日期的时间戳
	t := time.Date(2020, 3, 31, 23, 30, 0, 0, time.UTC)
	timestamp := t.Unix()
	fmt.Println(timestamp) //1585697400

	//获取当前时间的时间戳
	timestamp2 := time.Now().Unix()
	fmt.Println(timestamp2) //1585669151

	//当前时间的以纳秒为单位的时间戳
	timestamp3 := time.Now().UnixNano()
	fmt.Println(timestamp3) //1585669151296330900

	//时间间隔 相加
	now := time.Now()
	//当前时间加上一分钟
	t2 := now.Add(time.Minute)
	fmt.Println(now) //2020-03-31 23:43:35.0004791 +0800 CST m=+0.002999201
	fmt.Println(t2)  //2020-03-31 23:44:35.0004791 +0800 CST m=+60.002999201

	//计算两个时间的间隔
	d := t2.Sub(now)
	fmt.Println(d) //1m0s  相差一分钟

	//将指定时间转为时间戳格式
	beforetime := "2020-04-08 00:00:00"                             //待转化为时间戳的字符串
	timeLayout := "2006-01-02 15:04:05"                             //转化所需模板
	loc := time.Now().Location()                                    //获取时区
	theTime, _ := time.ParseInLocation(timeLayout, beforetime, loc) //使用模板在对应时区转化为time.time类型
	aftertime := theTime.Unix()                                     //转化为时间戳 类型是int64
	fmt.Println(theTime)                                            //打印输出theTime 2020-04-08 00:00:00 +0800 CST
	fmt.Println(aftertime)                                          //打印输出时间戳 1586275200

	//再将时间戳转换为日期
	dataTimeStr := time.Unix(aftertime, 0).Format(timeLayout) //设置时间戳 使用模板格式化为日期字符串
	fmt.Println(dataTimeStr)
}
