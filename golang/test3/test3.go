package main

import "fmt"

func main() {
	a := "HI,世界"
	fmt.Println(a)
	n := 0
	for range a {
		n++
	}
	fmt.Println(len(a), n)

	array := []int{5, 6, 7}
	fmt.Println(array, len(array), cap(array))
	array = append(array, 8, 9)
	fmt.Println(array, len(array), cap(array))
	array = append(array, 10, 11)
	fmt.Println(array, len(array), cap(array))

	array2 := make([]int, 10)
	fmt.Println(array2, len(array2), cap(array2))
	fmt.Println(&array2[0])
	fmt.Println(&array2[1])

	array3 := []string{"fb", "yt"}
	fmt.Println(array3, len(array3), cap(array3))

}
