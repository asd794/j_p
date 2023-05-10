package main

import (
	"fmt"
	"log"
)

func main() {
	var a = [10]int{}
	for i := 0; i < 10; i++ {
		a[i] = i + 1
	}
	fmt.Println(len(a))
	fmt.Println(a)

	array := [3]int{5, 80, 22}
	fmt.Println(len(array))
	fmt.Println(array)
	for x := 0; x < len(array); x++ {
		fmt.Println(array[x])
	}

	num := []int{100, 99, 98}
	for i, abc := range num {
		log.Println(i, abc)
		fmt.Println(i, abc)
	}
	log.SetFlags(1)
}
