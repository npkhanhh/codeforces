package main

import "fmt"

func main() {
	var n, h int
	fmt.Scan(&n, &h)
	res := 0
	var t int
	for i := 0;i<n;i++{
		fmt.Scan(&t)
		if t <= h {
			res += 1
		} else {
			res += 2
		}
	}
	fmt.Println(res)
}
