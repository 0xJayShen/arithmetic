package main

import (
	"fmt"
)

func binary_search(list []int, target int) (int) {
	low := 0
	height := len(list)

	for low < height {
		mid := (low + height) / 2

		guess := list[mid]

		if guess > target {
			height = mid
		} else if guess < target {
			low = mid + 1
		} else {
			fmt.Println(" 猜的数字在第---", mid)
			return mid
		}
		fmt.Println(low, height)
	}

	fmt.Println("数字不存在")
	return -1
}

func main() {
	mylist := []int{1, 3, 6, 9, 12, 18, 19, 33}
	binary_search(mylist, 33)
}
