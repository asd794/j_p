package main

import "fmt"

func main() {
	var x int
	fmt.Print("輸入第一個數值x：")
	fmt.Scanln(&x)
	var y int
	fmt.Print("輸入第二個數值y：")
	fmt.Scanln(&y)
	var sum int = x + y
	println(" x + y =", sum)

	var (
		a int
		b int
	)

	fmt.Println("輸入兩筆數字,使用空白隔開：")
	fmt.Scanln(&a, &b)
	var sum2 int = a + b
	println("a + b =", sum2)
}
