package main

import "fmt"

func main() {
	array := [3]int{5, 80, 22}
	fmt.Println(len(array))
	fmt.Println(array)
	for x := 0; x < len(array); x++ {
		fmt.Println(array[x])
	}

}
