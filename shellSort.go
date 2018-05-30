package main

import "fmt"

func ShellSort(arr []int) {
	n := len(arr)
	gap := n / 2

	for gap >= 1{
		for i := gap; i < n; i++ {
			j := i
			for j >= gap && arr[j] < arr[j-gap] {
				arr[j], arr[j-gap] = arr[j-gap], arr[j]
				j -= gap
			}

		}
		gap /= 2
	}

	fmt.Println(arr)
}

func main() {
	ShellSort([]int{4, 5, 1, 4, 6, 7, 8, 1, 0, 74, 1, 7})
}
