package main

import (
	"log"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/16 16:23
*/

func main() {
	////控制台打印日志    严重程度递增
	//log.Println("打印Println日志信息")
	//log.Panic("打印Panic日志信息")
	//log.Fatal("打印Fatal日志信息")

	//输出日志到指定文件
	file, _ := os.OpenFile("./25_log/log.log", os.O_APPEND|os.O_CREATE, 0777) //参数：文件路径，打开方式，权限（linux起作用）
	logger := log.New(file, "[Info] ", log.LstdFlags)
	logger.Println("打印 Println 日志")
	//logger.Panic("打印 Panic 日志")
	//logger.Fatal("打印 Fatal 日志")
}
