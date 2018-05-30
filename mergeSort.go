package main

import "fmt"

func MergeSort(arr []int) []int {

	num := len(arr) / 2

	if len(arr) <= 1 {
		return arr
	}

	left := MergeSort(arr[:num])

	right := MergeSort(arr[num:])

	l, r := 0, 0
	var result []int

	for l < len(left) && r < len(right) {
		if left[l] < right[r] {
			result = append(result, left[l])
			l++
		} else {
			result = append(result, right[r])
			r++
		}
	}

	result = append(result, right[r:]...)
	result = append(result, left[l:]...)

	return result
}

func main() {
	result := MergeSort([]int{1, 4, 7, 2, 9, 22, 5, 0, 7})
	fmt.Println(result)
}
