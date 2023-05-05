package main

import (
	"fmt"
	"log"
)

func main() {
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
