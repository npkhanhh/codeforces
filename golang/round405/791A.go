package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	res := 0
	for i := 1; i <= 10; i++ {
		a *= 3
		b *= 2
		if a > b {
			res = i
			break
		}
	}
	fmt.Println(res)
}
