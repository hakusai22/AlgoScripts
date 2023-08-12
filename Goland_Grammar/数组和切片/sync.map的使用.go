package main

import (
	"fmt"
	"sync"
)

// 声明sync.Map
var syncmap sync.Map

func main() {

	//Store方法将键值对保存到sync.Map
	syncmap.Store("zhangsan", 97)
	syncmap.Store("lisi", 100)
	syncmap.Store("wangmazi", 200)

	// Load方法获取sync.Map 键所对应的值
	fmt.Println(syncmap.Load("lisi"))

	// Delete方法键删除对应的键值对
	syncmap.Delete("lisi")

	// Range遍历所有sync.Map中的键值对
	syncmap.Range(func(k, v interface{}) bool {
		fmt.Println(k, v)
		return true
	})

}
