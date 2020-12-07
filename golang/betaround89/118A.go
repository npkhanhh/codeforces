package main

import (
	"fmt"
	"strings"
)

func main()  {
	var s string
	fmt.Scan(&s)
	s = strings.ToLower(s)
	var result strings.Builder
	for _, val := range s {
		if val != 'a' && val != 'o' && val != 'y' && val != 'e' && val != 'u' && val != 'i' {
			result.WriteString(".")
			result.WriteString(string(val))

		}
	}
	fmt.Println(result.String())
}
