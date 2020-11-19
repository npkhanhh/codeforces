package main

import (
	"fmt"
	"strings"
)

func main() {
	var a, b string

	fmt.Scan(&a)
	fmt.Scan(&b)
	a = strings.ToLower(a)
	b = strings.ToLower(b)
	fmt.Println(strings.Compare(a, b))
}

