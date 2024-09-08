package main

import (
	"AlgoScripts/Golang_Basis/04_network/webSocket/common"
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 01:51
   @题目     :
   @参考     :
   @时间复杂度:
*/

func main() {
	router := mux.NewRouter()
	go common.H.Run()
	router.HandleFunc("/ws", common.Myws)
	if err := http.ListenAndServe("127.0.0.1:8080", router); err != nil {
		fmt.Println("err:", err)
	}
}
