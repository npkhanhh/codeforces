package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	res := 0
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		if s[1] == '+' {
			res++
		} else {
			res--
		}
	}
	fmt.Println(res)

}
