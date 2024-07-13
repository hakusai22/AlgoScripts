/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/24 00:12
*/

package main

import (
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/hello", func(writer http.ResponseWriter, request *http.Request) {
		f, _ := os.Open("./hello.txt")
		buf := make([]byte, 1024)
		// 内核拷贝到buf
		n, _ := f.Read(buf)
		// buf拷贝到内核
		writer.Write(buf[:n])
	})
	http.ListenAndServe(":8080", http.DefaultServeMux)
}
