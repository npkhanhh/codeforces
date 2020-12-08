package main

import "fmt"

func main()  {
	var s, t string
	fmt.Scan(&s)
	t = "hello"
	j := 0
	for i, _ := range s {
		if s[i] == t[j] {
			j += 1
		}
		if j == 5 {
			break
		}
	}
	if j == 5 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
