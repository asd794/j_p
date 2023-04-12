package main

import "fmt"

func main() {

	// var z int = 0
	// for true {
	// 	z++
	// 	fmt.Println(z)
	// }

	// var i int = 0
	// for i < 3 {
	// 	fmt.Println(i)
	// 	i++
	// }

	// var i int
	// for i = 0; i < 3; i++ {
	// 	fmt.Println(i)
	// }

	var (
		i   int
		sum int = 0
	)
	for i = 1; i <= 50; i++ {
		sum = sum + i
	}
	fmt.Println(sum)
}
