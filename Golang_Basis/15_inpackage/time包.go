package main

import (
	"fmt"
	"time"
)

// time包操作的都是时间，时间的单位都包括年，月，日，时，分，秒，毫秒，微妙，纳秒，皮秒。
func main() {
	//获取当前时间
	t := time.Now()
	fmt.Println(t) //2020-03-31 21:26:01.7307507 +0800 CST m=+0.001999001
	//获取的时间后面的信息是时区

	//上面的时间看起来不是很方便 于是需要格式化时间
	s := t.Format("2006年1月2日 15:04:05")
	fmt.Println(s)

	now := time.Now()
	fmt.Println(now)
	t1 := time.Date(2022, 3, 27, 1, 25, 36, 0, time.UTC)
	t2 := time.Date(2022, 3, 27, 1, 25, 36, 0, time.UTC)
	fmt.Println(t1)
	fmt.Println(t2)
	fmt.Println(t1.Year(), t1.Month(), t1.Day(), t1.Hour(), t1.Minute())
	fmt.Println(t1.Format("2006-01-02 15:04:05"))
	diff := t2.Sub(t1)
	fmt.Println(diff)
	fmt.Println(diff.Minutes(), diff.Seconds())
	fmt.Println(now.Unix())

	s11 := t.Format("2006-1-2 15:04:05")
	fmt.Println(s11) //打印出的格式就是当前的时间 2020-3-31 23:08:35

	s22 := t.Format("2006/1/2")
	fmt.Println(s22) //打印出的格式就是当前的年月日 2020/3/31

	//字符串类型的时间
	str := "2020年3月31日"
	//第一个参数是模板,第二个是要转换的时间字符串
	s33, _ := time.Parse("2006年1月2日", str)
	fmt.Println(s33) //打印出的格式就是2020-03-31 00:00:00 +0000 UTC

	//获取年月日信息
	year, month, day := time.Now().Date()
	fmt.Println(year, month, day) //2020 March 31

	//获取时分秒信息
	hour, minute, second := time.Now().Clock()
	fmt.Println(hour, minute, second) //23 23 54

	//获取今年过了多少天了
	tday := time.Now().YearDay()
	fmt.Println(tday) //91  (今年已经过了91天了)

	//获取今天是星期几
	weekday := time.Now().Weekday()
	fmt.Println(weekday) //Tuesday
}
