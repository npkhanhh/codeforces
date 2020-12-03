package main

import "fmt"

func main()  {
	var n int
	var s string
	fmt.Scan(&n)
	fmt.Scan(&s)
	d := 0
	a := 0
	for _, c := range s {
		if c == 'A' {
			a += 1
		} else {
			d += 1
		}
	}
	if d > a {
		fmt.Println("Danik")
	} else if d == a {
		fmt.Println("Friendship")
	} else {
		fmt.Println("Anton")
	}
}
