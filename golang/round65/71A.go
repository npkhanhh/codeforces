package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		if len(s) <= 10 {
			fmt.Println(s)
		} else {
			fmt.Print(string(s[0]))
			fmt.Print(len(s)-2)
			fmt.Println(string(s[len(s)-1]))
		}

	}

}
