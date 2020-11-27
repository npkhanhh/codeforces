package main

import "fmt"

func main() {
	var n, a, b int
	fmt.Scan(&n)
	t := 0
	res := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&a, &b)
		t -= a
		t += b
		if t > res {
			res = t
		}
	}
	fmt.Println(res)
}

