package json_impl

import (
	"errors"
	"fmt"
	"reflect"
	"strconv"
	"strings"
	"testing"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 17:26
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

// Unmarshal 反序列化
func Unmarshal(data []byte, v interface{}) error {
	parsedData, err := parseJSON(string(data))
	if err != nil {
		return err
	}

	val := reflect.ValueOf(v).Elem()
	typ := val.Type()

	for i := 0; i < val.NumField(); i++ {
		fieldVal := val.Field(i)
		fieldType := typ.Field(i)

		// 获取 JSON 标签
		tag := fieldType.Tag.Get("json")
		if tag == "" {
			tag = fieldType.Name
		}

		// 从解析的数据中获取值
		if value, ok := parsedData[tag]; ok {
			switch fieldVal.Kind() {
			case reflect.String:
				fieldVal.SetString(value)
			case reflect.Int:
				intValue, err := strconv.Atoi(value)
				if err != nil {
					return err
				}
				fieldVal.SetInt(int64(intValue))
			default:
				return fmt.Errorf("unsupported field type: %s", fieldVal.Kind())
			}
		}
	}

	return nil
}

// 简易版 JSON 解析器，仅支持 string/int 且不考虑嵌套
func parseJSON(data string) (map[string]string, error) {
	result := make(map[string]string)

	data = strings.TrimSpace(data)
	if len(data) < 2 || data[0] != '{' || data[len(data)-1] != '}' {
		return nil, errors.New("invalid JSON")
	}

	data = data[1 : len(data)-1]
	parts := strings.Split(data, ",")
	for _, part := range parts {
		kv := strings.SplitN(part, ":", 2)
		if len(kv) != 2 {
			return nil, errors.New("invalid JSON")
		}

		k := strings.Trim(strings.TrimSpace(kv[0]), `"`)
		v := strings.Trim(strings.TrimSpace(kv[1]), `"`)

		result[k] = v
	}

	return result, nil
}

func TestName2(t *testing.T) {
	jsonData := `{"name":"hakusai22","age":24,"Email":"hakusai22@qq.com"}`
	var user User
	err := Unmarshal([]byte(jsonData), &user)
	if err != nil {
		fmt.Println("Error unmarshal from JSON:", err)
		return
	}
	fmt.Printf("User struct: %+v\n", user)
}
