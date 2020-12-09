package main

import "fmt"

func main()  {
	var n int
	fmt.Scan(&n)
	a := []int{4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777}
	for _, val := range a {
		if n % val == 0 {
			fmt.Println("YES")
			return
		}
	}
	fmt.Println("NO")
}
