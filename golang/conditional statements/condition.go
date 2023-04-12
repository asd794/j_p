package main

import (
	"fmt"
)

func main() {

	var score int
	fmt.Print("請輸入分數：")
	fmt.Scanln(&score)
	if score < 0 || score > 100 {
		fmt.Println("您輸入的分數為", score, ",輸入錯誤,請輸入範圍0~100.")
	} else if score > 59 {
		fmt.Println("分數於60~100之間,恭喜及格", score, "分.")
	} else {
		fmt.Println("分數低於60,不及格", score, "分.")
	}

}
