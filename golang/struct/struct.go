package main

import "fmt"

type Person struct {
	name string
	age  int
}

func main() {
	var p1 Person = Person{"小明", 18}
	fmt.Println(p1.name, p1.age)
	var p2 Person = Person{age: 40, name: "老王"}
	fmt.Println(p2.name, p2.age)
	p2.name = "老黃"
	fmt.Println(p2.name, p2.age)
}
