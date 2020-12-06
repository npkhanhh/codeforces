package main

import "fmt"

func main()  {
	var n, x, y, z, tx, ty, tz int
	fmt.Scan(&n)
	for i := 0; i<n; i++ {
		fmt.Scan(&tx, &ty, &tz)
		x += tx
		y += ty
		z += tz
	}
	if x == 0 && y == 0 && z == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
