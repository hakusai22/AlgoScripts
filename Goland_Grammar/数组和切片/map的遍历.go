package main

import "fmt"

func main() {
	//map的遍历
	//因为map是无序的 如果需要获取map中所有的键值对
	//可以使用 for range
	map1 := make(map[int]string)
	map1[1] = "张无忌"
	map1[2] = "张三丰"
	map1[3] = "常遇春"
	map1[4] = "胡青牛"

	m := make(map[string]string)
	m["asdfasd"] = "fasdfasdf"
	for s, s2 := range m {
		fmt.Println(s, s2)
	}
	//遍历map
	for key, val := range map1 {
		fmt.Println(key, val)
	}
}
