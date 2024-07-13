module Go_Study

//module: 用于定义当前项目的模块路径
//go:标识当前Go版本.即初始化版本
go 1.21

// indirect: 示该模块为间接依赖，也就是在当前应用程序中的 import 语句中，并没有发现这个模块的明确引用
// require: 当前项目依赖的一个特定的必须版本
require github.com/emirpasic/gods v1.18.1
