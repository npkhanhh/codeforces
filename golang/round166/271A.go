package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for t:=n+1 ;; t++ {
		m := make(map[int]bool)
		a := t
		result := true
		for i := 0; i < 4; i++ {
			z := a % 10
			if _, ok := m[z]; ok {
				result = false
				break
			} else {
				m[z] = true
			}
			a = a / 10
		}
		if result {
			fmt.Println(t)
			break
		}
	}
}
