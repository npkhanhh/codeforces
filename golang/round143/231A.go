package main

import "fmt"

func main() {
	var n int
	var p int
	res := 0
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		t := 0
		for j:= 0; j < 3; j++ {
			fmt.Scan(&p)
			t += p
		}
		if t >= 2 {
			res += 1
		}
	}
	fmt.Println(res)

}
