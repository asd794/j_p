package main

import "fmt"

// func showhello(msg string) {
// 	if msg == "hello1" {
// 		return
// 	}
// 	fmt.Println("hello2")
// }

// func add(n1 int, n2 int) int {
// 	var sum int = n1 + n2
// 	return sum
// }

func r() (int, float32, string) {
	return 5, 1.2, "hello"
}

func main() {

	// showhello("hello1")
	// showhello("hello2")

	// var total int = add(33, 22)
	// fmt.Println(total)

	var (
		x int
		y float32
		z string
	)
	x, y, z = r()

	fmt.Println(x, y, z)
	fmt.Println(y)

}
