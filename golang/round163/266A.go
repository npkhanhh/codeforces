package main

import "fmt"

func main() {
	var n int
	var s string
	fmt.Scan(&n)
	fmt.Scan(&s)
	res := 0
	for i := 1; i < n; i++ {
		if s[i] == s[i-1] {
			res += 1
		}
	}
	fmt.Println(res)
}
