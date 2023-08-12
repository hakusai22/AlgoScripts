package main

import "fmt"

func main() {
	//创建一个map存储第一个人的信息
	map1 := make(map[string]string)
	map1["name"] = "张无忌"
	map1["sex"] = "男"
	map1["age"] = "21"
	map1["address"] = "明教"

	//如果需要存储第二个人的信息则需要重新创建map
	map2 := make(map[string]string)
	map2["name"] = "周芷若"
	map2["sex"] = "女"
	map2["age"] = "22"
	map2["address"] = "峨眉山"

	//将map存入切片 slice中

	s1 := make([]map[string]string, 0, 2)
	s1 = append(s1, map1)
	s1 = append(s1, map2)

	//遍历map
	for key, val := range s1 {
		fmt.Println(key, val)
	}
}
