package main

import "fmt"

func main() {
	var n, t int
	var s []byte
	fmt.Scan(&n, &t)
	fmt.Scan(&s)
	for j := 0; j < t; j++ {
		for i := 0; i < n-1; i++ {
			if s[i] == 'B' && s[i+1] == 'G' {
				s[i] = 'G'
				s[i+1] = 'B'
				i += 1
			}
		}
	}
	fmt.Println(string(s))
}
