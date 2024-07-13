/*
 * @Author: hakusai
 * @Date: 2023-05-17 22:26:50
 * @LastEditTime: 2023-05-17 22:27:03
 * @Description:
 */
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var people []map[string]interface{}
	var m1 map[string]interface{}
	m1 = make(map[string]interface{})
	m1["name"] = "hello one"
	m1["age"] = 10
	m1["address"] = "US"
	people = append(people, m1)
	var m2 map[string]interface{}
	m2 = make(map[string]interface{})
	m2["name"] = "hello two"
	m2["age"] = 20
	m2["address"] = [2]string{"Canada", "China"}
	people = append(people, m2)
	jsonSlice, err := json.Marshal(people) //go自带包json里的Marshal()方法将切片序列化成字符串切片
	if err != nil {
		fmt.Printf("序列化错误，err:=%v", err)
		return
	}
	fmt.Println(string(jsonSlice)) //返回的是切片  要记得转换成字符串类型
}
