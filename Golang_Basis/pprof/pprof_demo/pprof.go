package main

import (
	"fmt"
	_ "github.com/mkevac/debugcharts" // 添加后可以查看几个实时图表数据
	"net/http"
	_ "net/http/pprof"
	"time"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 18:58
*/

func memoryLeak() {
	var s [][]int
	for i := 0; i < 1000; i++ {
		s = append(s, make([]int, 1000))
	}
}

func main() {
	http.HandleFunc("/manyGo", func(writer http.ResponseWriter, request *http.Request) {
		fmt.Println("manyGo...")
		go func() {
			time.Sleep(30 * time.Minute)
		}()
		_, _ = writer.Write([]byte("Hello"))
	})
	http.HandleFunc("/memoryLeak", func(writer http.ResponseWriter, request *http.Request) {
		fmt.Println("memoryLeak...")
		memoryLeak()
		_, _ = writer.Write([]byte("Hello"))
	})
	_ = http.ListenAndServe(":8001", nil)
}
