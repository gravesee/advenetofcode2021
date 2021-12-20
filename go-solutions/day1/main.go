package main

import (
	"aoc/day1/solution"
	"fmt"
	"log"
	"strconv"
)

func main() {
	data, err := solution.ReadLines("data/test.txt")
	if err != nil {
		log.Fatal(err)
	}

	var slice = make([]int, len(data))
	for i, s := range data {
		slice[i], err = strconv.Atoi(s)
		if err != nil {
			log.Fatal(err)
		}
	}

	// solution 1
	var inc int = 0
	for i, num := range slice {

		if i == 0 {
			continue
		}
		if num > slice[i-1] {
			inc += 1
		}
	}
	fmt.Println(inc)

	// solution 2
	inc = 0
	for i := range slice {

		if i < 3 {
			continue
		}
		if (slice[i-2] + slice[i-1] + slice[i]) > (slice[i-3] + slice[i-2] + slice[i-1]) {
			inc += 1
		}
	}
	fmt.Println(inc)

}
