package main

import "fmt"

func main() {
	app := []string{"FB", "IG", "YT"}
	for i := 0; i < len(app); i++ {
		fmt.Println(i, app[i])
	}
	for n, apex := range app {
		fmt.Println(n, apex)
	}
}
