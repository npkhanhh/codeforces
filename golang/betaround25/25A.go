package main

import "fmt"

func main() {
	var n int
	var t int
	fmt.Scan(&n)
	even := -1
	odd := -1
	c_odd := 0
	c_even := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&t)
		if t%2 == 0 {
			even = i + 1
			c_even += 1
		} else if t%2 == 1 {
			odd = i + 1
			c_odd += 1
		}

	}
	if c_even == 1 {
		fmt.Println(even)
	} else {
		fmt.Println(odd)
	}
}
