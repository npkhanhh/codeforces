package main

import (
	"fmt"
	"math"
)

func main() {
	var v int
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			fmt.Scan(&v)
			if v == 1 {
				fmt.Println(math.Abs(float64(i-2)) + math.Abs(float64(j-2)))
				return
			}
		}
	}

}
