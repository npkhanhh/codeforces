package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	var p, q int
	res := 0
	for i := 0;i < n; i++ {
		fmt.Scan(&p, &q)
		if q - p >= 2 {
			res += 1
		}
	}
	fmt.Println(res)
}
