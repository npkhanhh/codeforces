package main

import (
	"fmt"
	"strings"
)

func main()  {
	var s string
	m := make(map[uint8]int)
	fmt.Scan(&s)
	s = strings.TrimSuffix(s, "\n")
	for i := 0; i<len(s); i++ {
		m[s[i]] = 1
	}
	if len(m) % 2 == 1 {
		fmt.Println("IGNORE HIM!")
	} else {
		fmt.Println("CHAT WITH HER!")
	}
}
