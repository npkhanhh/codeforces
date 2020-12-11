package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	c := 1
	res := "NO"
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			c += 1
			if c == 7 {
				res = "YES"
				break
			}
		} else {
			c = 1
		}
	}
	fmt.Println(res)
}
