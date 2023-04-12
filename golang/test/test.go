package main

import (
	"fmt"
	"time"
)

func main() {
	const PI = 3.14159
	const HELLO = "HELLO WORLD"
	fmt.Println(time.Now())

	// timeyear := time.Now().Year()
	x, y := 1, 2
	x, z := 3, 4
	var sum float32
	sum = PI

	fmt.Println(x, y, z, HELLO, sum)

}
