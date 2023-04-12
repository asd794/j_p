package main

import "fmt"

func add(xPtr *int) {
	*xPtr += 10
	fmt.Println("add function", *xPtr)

}

func main() {
	var x int = 10
	fmt.Println("最原始", x, &x)
	add(&x)
	fmt.Println("main function", x)

	var msg string
	var msgPtr *string = &msg
	fmt.Scanln(msgPtr)
	fmt.Println(msgPtr, &msg)
	fmt.Println(*msgPtr, msg)

	// var loop int = 0
	// for true {
	// 	loop++
	// 	fmt.Println(loop)
	// 	if loop == 10000 {
	// 		break
	// 	}
	// }

	// var x int = 3
	// var xPtr *int = &x
	// fmt.Println(x, xPtr, *xPtr)

	// var y string = "指標"
	// var yPtr *string = &y
	// fmt.Println(y, yPtr, *yPtr)

}
