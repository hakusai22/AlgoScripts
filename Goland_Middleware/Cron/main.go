package main

import (
	"fmt"
	"github.com/roylee0704/gron"
	"sync"
	"time"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/08/11 22:48
*/

func main() {
	var wg sync.WaitGroup
	wg.Add(1)

	c := gron.New()
	c.AddFunc(gron.Every(5*time.Second), func() {
		fmt.Println("runs every 5 seconds.")
	})
	c.Start()

	wg.Wait()
}
