package main

import (
	"fmt"
)

func main() {
	var x int
	fmt.Print("請輸入 1 2 3 其中一個數字: ")
	fmt.Scanln(&x)
	switch x {
	case 1:
		fmt.Println("數字1")
	case 2:
		fmt.Println("數字2")
	case 3:
		fmt.Println("數字3")
	default:
		fmt.Println("1 2 3以外的數字")

	}

}
