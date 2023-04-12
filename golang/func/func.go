package main

import "fmt"

func test(msg string) {
	fmt.Println("Hello,", msg)
}
func sum(x int, y int) {
	fmt.Println(x + y)
}
func fortotal() {
	var a int
	var z int
	fmt.Print("a = ")
	fmt.Scanln(&a)
	fmt.Print("z = ")
	fmt.Scanln(&z)
	var i int
	var sum int = 0
	for i = a; i <= z; i++ {
		sum += i
	}
	fmt.Println(a, "加到", z, "總共為:", sum)
}

func main() {
	test("Jay")
	test("asd")
	sum(2, 3)
	fortotal()

}
