package main

import "fmt"

type Name struct {
	a string
	b bool
	c int
}

func main() {
	fmt.Printf("%v \t", Name{})
	fmt.Printf("%+v \t", Name{})
	fmt.Printf("%#v \n", Name{})
	var n1 Name = Name{"你好", true, 100}
	fmt.Println(n1.a, n1.b, n1.c)

	s1 := "I"
	s2 := "am"
	s3 := "string"

	str1 := fmt.Sprintln(s1, s2, s3)
	fmt.Println(str1)
	str2 := fmt.Sprintf(s1, s2, s3)
	fmt.Println(str2)
	str3 := fmt.Sprint(s1, s2, s3)
	fmt.Println(str3)

}
