/*
 * @Author: hakusai
 * @Date: 2023-04-24 16:40:15
 * @LastEditTime: 2023-04-24 17:51:51
 */
package main

import "fmt"

type MyObject struct {
	ID    int
	Name  string
	Value float64
}

func main() {
	myObjects := []MyObject{
		{ID: 1, Name: "python_object 1", Value: 3.14},
		{ID: 2, Name: "python_object 2", Value: 6.28},
		{ID: 3, Name: "python_object 3", Value: 9.42},
	}

	IDs := Map(myObjects, func(obj MyObject) int {
		return obj.ID
	})

	names := Map(myObjects, func(obj MyObject) string {
		return obj.Name
	})
	fmt.Println(names)

	fmt.Println(IDs)
}

func Map[T, U any](objects []T, f func(T) U) []U {
	mappedValues := make([]U, len(objects))
	for i, obj := range objects {
		mappedValues[i] = f(obj)
	}
	return mappedValues
}
