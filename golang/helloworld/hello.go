package main

import (
	"fmt"
)

// https://ithelp.ithome.com.tw/articles/10214311
// var year int = 2020
// var name string = "Iron man"

// var price, movie = 2020, "Iron man"

// var (
// 	a int
// 	b string
// 	c []float32
// 	d func() bool
// )

func main() {

	// abc := 1
	// fmt.Println(abc)
	// fmt.Println(123456789)
	// fmt.Println("測試567")
	// fmt.Println(true)
	// fmt.Println('a')
	// fmt.Println("abc")
	// fmt.Printf("%d", year)

	var x int
	var y string

	x = 4
	fmt.Println(x)
	x = 10
	fmt.Println(x)
	y = "Hello"
	fmt.Println(y)

	var z float32 = 123.456
	fmt.Println(z)
	var test bool = false
	fmt.Println(test)
	var c rune = 'b'
	fmt.Println(c)

	var a int = 1000
	fmt.Println(a)

}
