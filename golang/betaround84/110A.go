package main

import (
	"fmt"
	"strconv"
)

func main()  {
	var s string
	fmt.Scan(&s)
	t := 0
	res := "YES"
	for i := 0; i<len(s); i++ {
		if s[i] == '4' || s[i] == '7' {
			t += 1
		}
	}
	z := strconv.Itoa(t)
	for i := 0; i< len(z); i++ {
		if z[i] != '4' && z[i] != '7' {
			res = "NO"
			break
		}
	}
	fmt.Println(res)
}
