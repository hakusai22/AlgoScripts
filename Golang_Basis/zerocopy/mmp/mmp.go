/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/24 00:15
*/

package main

func main() {
	//http.HandleFunc("/mmap", func(writer http.ResponseWriter, request *http.Request) {
	//	f, _ := os.Open("./hello.txt")
	//	data, err := syscall.Mmap(int(f.Fd()), 0, 12, syscall.PROT_READ, syscall.MAP_SHARED) // mmap返回了一个data的字节数组，这个字节数组的内容就是映射了文件内容
	//	/*
	//	   syscall.Mmap(int(f.Fd()), 0, 12, syscall.PROT_READ, syscall.MAP_SHARED)
	//	   mmap涉及的参数含义:
	//	   第一个：要映射的文件描述符。
	//	   第二、三个：映射的范围是从0个字节到第12个字节（也就是 Hello World!）。
	//	   第四个:代表映射的后的内存区域是只读的，类似的参数还有 syscall.PROT_WRITE表示内存区域可以被写入，syscall.PROT_NONE表示内存区域不可访问。
	//	   第五个：映射的内存区域可以被多个进程共享，这样一个进程修改了这个内存区域的数据，对其他进程是可见的，并且修改后的内容会自动被操作系统同步到磁盘文件里。
	//	*/
	//	if err != nil {
	//		panic(err)
	//	}
	//	writer.Write(data)
	//})
	//http.ListenAndServe(":8080", http.DefaultServeMux)
}
