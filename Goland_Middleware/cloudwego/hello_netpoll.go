package cloudwego

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/04/26 10:51
*/

import "github.com/cloudwego/netpoll"

func main() {
	_, err := netpoll.CreateListener("tcp", "127.0.0.1")
	if err != nil {
		panic("error")
	}

}
