package main

import (
	"fmt"
	"math"
)

func main()  {
	var n, m, a int
	fmt.Scan(&n, &m, &a)
	fmt.Printf("%d\n", int64(math.Ceil(float64(n) / float64(a))) * int64(math.Ceil(float64(m) /float64(a))))
}
