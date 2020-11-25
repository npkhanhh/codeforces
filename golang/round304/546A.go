package main

import "fmt"

func main() {
	var k, n, w int
	fmt.Scan(&k, &n, &w)
	total := w*(w+1)*k/2
	res := 0
	if total > n {
		res = total - n
	}
	fmt.Println(res)
}
