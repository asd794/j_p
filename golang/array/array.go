package main

import (
	"fmt"
)

// func arrtest(a int) {

// }

func main() {
	var arr [4]int = [4]int{6, 1, 4, 55}
	fmt.Println(arr)
	var i int
	for i = 0; i < len(arr); i++ {
		println("arr[", i, "]=", arr[i])
	}

	var names [4]string = [4]string{"John", "Sam", "Jeff", "Zeka"}
	fmt.Println(names)

	var grades [10]int = [10]int{59, 88, 33, 45, 68, 63, 90, 85, 84, 88}
	var y int
	var sum int = 0
	for y = 0; y < len(grades); y++ {
		sum += grades[y]
	}
	fmt.Println(sum)

	var input [3]int
	var x int = 0
	var avg int = 0
	fmt.Println("請輸入三筆資料算平均:")
	for x = 0; x < len(input); x++ {
		fmt.Scanln(&input[x])
		avg += input[x]
	}
	fmt.Println("平均為:", avg/len(input))
	fmt.Println(input)
}
