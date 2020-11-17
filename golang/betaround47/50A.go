package main

import "fmt"

func main(){
	var m, n int
	fmt.Scanf("%d %d", &m, &n);
	res := m*n
	if res % 2 == 1 {
		res -= 1
	}
	res /= 2
	fmt.Println(res)
}
