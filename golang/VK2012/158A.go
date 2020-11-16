package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d", &n, &k)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	score := a[k-1]
	if score == 0 {
		score = 1
	}
	var i int
	for i = 0; i < n && a[i] >= score; i++ {}
	fmt.Println(i)
}
