package main

import (
	"encoding/json"
	"fmt"
)

type userInfo struct {
	Name  string
	Age   int `json:"age"`
	Hobby []string
}

func main() {
	info := userInfo{Name: "yin", Age: 18, Hobby: []string{"Goland", "TypeScript"}}
	buf, err := json.Marshal(info)
	if err != nil {
		panic(err)
	}
	fmt.Println(buf)
	fmt.Println(string(buf))

	buf, err = json.MarshalIndent(info, "", "\t")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(buf))

	var b userInfo
	err = json.Unmarshal(buf, &b)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%#v\n\n", b)
}
