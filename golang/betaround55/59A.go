package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main()  {
	var s string
	fmt.Scan(&s)
	u := 0
	l := 0
	for _, c := range s {
		if unicode.IsUpper(c) {
			u += 1
		} else {
			l += 1
		}
	}
	if u > l {
		fmt.Println(strings.ToUpper(s))
	} else {
		fmt.Println(strings.ToLower(s))
	}

}
