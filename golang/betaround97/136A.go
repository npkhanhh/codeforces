package main

import (
	"fmt"
	"strings"
)

func main()  {
	var n, t int
	fmt.Scan(&n)
	var res = make([]int, n)
	for i := 0; i<n; i++ {
		fmt.Scan(&t)
		res[t-1] = i + 1
	}
	fmt.Println(strings.Trim(strings.Join(strings.Fields(fmt.Sprint(res)), " "), "[]"))
}
