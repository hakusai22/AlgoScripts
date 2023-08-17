package _1_hellworld

import "github.com/gin-gonic/gin"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/16 16:31
*/

// 官网 https://gin-gonic.com/zh-cn/docs/examples/without-middleware/
func main() {
	engine := gin.Default()

	//GET请求 http://localhost:8888/hello
	engine.GET("/hello", func(c *gin.Context) {
		//返回字节数组
		c.Writer.Write([]byte("hello you are welcome! \n"))

		//返回状态 + json对象(常用)
		c.JSON(200, gin.H{
			"message": "欢迎访问！",
		})
	})
	engine.Run(":8888") // 监听并在 0.0.0.0:8888 上启动服务

}
