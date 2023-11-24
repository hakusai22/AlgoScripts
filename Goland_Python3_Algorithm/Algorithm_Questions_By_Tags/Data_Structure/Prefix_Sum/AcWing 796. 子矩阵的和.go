package Prefix_Sum

import (
	"bufio"
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/16 12:22
*/

/**
bufio.NewScanner的底层buf数组有个最大缓存限制的，是64K，
也就是说按照标准的Scan，一行最多64K的数据大小，题目里如果超过这个范围，
比如一行20万数据，每个数据范围还是int32内的，那这就至少800K的大小了，
还没算上中间的空格，所以默认的buf空间肯定是不够的，
这时候需要调用Buffer方法，手动给Scanner分配一个满足题目空间的buf数组，其余照常。使用方法如下：
*/
func main() {
	sc := bufio.NewScanner(os.Stdin) // 实例化 NewScanner
	bs := make([]byte, 2000*1024)    // 缓存
	sc.Buffer(bs, len(bs))
	sc.Scan()              // Scan 方法 该方法好比 iterator 中的 Next 方法，默认ScanLines 返回一行文本，不包括行尾的换行符
	fmt.Println(sc.Text()) // 该方法应该在 Scan 调用后调用.Text 返回的是 string
}
