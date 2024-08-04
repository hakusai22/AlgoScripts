module Go_Study

//module: 用于定义当前项目的模块路径
//go:标识当前Go版本.即初始化版本
go 1.21

// indirect: 示该模块为间接依赖，也就是在当前应用程序中的 import 语句中，并没有发现这个模块的明确引用
// require: 当前项目依赖的一个特定的必须版本
require github.com/emirpasic/gods v1.18.1

require (
	github.com/aws/aws-sdk-go v1.54.20
	github.com/emersion/go-imap v1.2.1
	github.com/emersion/go-message v0.18.1
	github.com/emirpasic/gods/v2 v2.0.0-alpha
	github.com/go-ego/gse v0.80.2
	github.com/gorilla/mux v1.8.1
	github.com/gorilla/websocket v1.5.3
	github.com/sashabaranov/go-openai v1.26.3
	github.com/tealeg/xlsx v1.0.5
)

require (
	github.com/emersion/go-sasl v0.0.0-20200509203442-7bfe0ed36a21 // indirect
	github.com/jmespath/go-jmespath v0.4.0 // indirect
	github.com/vcaesar/cedar v0.20.1 // indirect
	golang.org/x/text v0.14.0 // indirect
)
