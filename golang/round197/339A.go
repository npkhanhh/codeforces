package main

import (
	"fmt"
	"sort"
	"strings"
	"strconv"
)

func main() {
	var t string
	fmt.Scan(&t)
	s := strings.Split(t, "+")
	res := make([]int, 0)
	for i := 0; i < len(s); i++ {
		a, _ := strconv.Atoi(s[i])
		res = append(res, a)
	}
	sort.Ints(res)
	fmt.Println(strings.Trim(strings.Join(strings.Fields(fmt.Sprint(res)), "+"), "[]"))

}
