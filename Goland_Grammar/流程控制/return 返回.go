package main

import "fmt"

func main() {
	a, b, c := myfunc()
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)
}

func myfunc() (a, b, c int) {
	a, b, c = 111, 222, 333
	return
}
