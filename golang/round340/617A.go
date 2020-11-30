package main

import "fmt"

func main() {
	var x int
	fmt.Scan(&x)
	a := 1
	if x%5 == 0 {
		a = 0
	}
	fmt.Println(x/5 + a)

}
