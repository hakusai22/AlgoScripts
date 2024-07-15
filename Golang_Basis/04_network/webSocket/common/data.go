package common

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 01:53
   @题目     :
   @参考     :
   @时间复杂度:
*/

type Data struct {
	Ip       string   `json:"ip"`
	User     string   `json:"user"`
	From     string   `json:"from"`
	Type     string   `json:"type"`
	Content  string   `json:"content"`
	UserList []string `json:"user_list"`
}
