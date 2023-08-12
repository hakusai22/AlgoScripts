package main

import "fmt"

func main() {
	var m1 map[int]string         //只是声明 nil
	var m2 = make(map[int]string) //创建
	m3 := map[string]int{"语文": 89, "数学": 23, "英语": 90}

	fmt.Println(m1 == nil) //true
	fmt.Println(m2 == nil) //false
	fmt.Println(m3 == nil) //false

	//map 为nil的时候不能使用 所以使用之前先判断是否为nil
	if m1 == nil {
		m1 = make(map[int]string)
	}

	//1存储键值对到map中  语法:map[key]=value
	m1[1] = "小猪"
	m1[2] = "小猫"

	//2获取map中的键值对  语法:map[key]
	val := m1[2]
	fmt.Println(val)

	//3判断key是否存在   语法：value,ok:=map[key]
	val, ok := m1[1]
	fmt.Println(val, ok) //结果返回两个值，一个是当前获取的key对应的val值。二是当前值否存在，会返回一个true或false。

	//4修改map  如果不存在则添加， 如果存在直接修改原有数据。
	m1[1] = "小狗"

	//5删除map中key对应的键值对数据 语法: delete(map, key)
	delete(m1, 1)

	//6 获取map中的总长度 len(map)
	fmt.Println(len(m1))
}
