package main

import "fmt"

func main() {
	//break ,continue

	// var x int
	// for x = 0; x < 5; x++ {
	// 	if x == 1 {
	// 		continue
	// 		// break
	// 	}
	// 	fmt.Println(x)
	// }

	// var x int
	// for x = 0; x < 11; x++ {
	// 	if x%2 == 0 {
	// 		continue
	// 	}
	// 	fmt.Println(x)
	// }

	var x int
	var sum int = 0
	for true {
		fmt.Scanln(&x)
		if x == 0 {
			break
		}
		sum += x
	}
	fmt.Println("Total:", sum)
}
