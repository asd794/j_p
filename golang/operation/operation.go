package main

func main() {
	var (
		a int
		b int

		// d int
		// e int
	)
	a = 1 + 2 + 3*5
	println(a)
	b = 10
	b += 5 * 5
	println(b)
	b -= 2 + 2
	println(b)
	b++
	println(b)
	println("目前a = ", a, ",b = ", b)
	var c bool = a > b
	println(c, !c)
	c = false || true
	println(c)
}
