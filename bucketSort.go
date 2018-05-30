package main

import "fmt"

//bucket = [0, 0,0, 0, 0, 0, 0,0, 0, 0]
//
//[0,0,0,1,0,0,0,0,0,0]
//bucket[3]
//
//[0,1,0,1,0,0,0,0,0,0]
//
//[0,1,0,1,0,0,1,0,0,0]
//
//[0,1,0,1,1,0,1,0,0,0]
//
//[0,1,0,1,1,0,1,0,0,1]
//
//[0,1,0,1,1,0,1,1,0,1]
//
//[0,1,0,1,2,0,1,1,0,1]
//
//[0,2,0,1,2,0,1,1,0,1]

func BucketSort(arr []int) []int {
	max := 0

	for i := 0; i < len(arr); i++ {
		if arr[i] > max {
			max = arr[i]
		}
	}

	var bucket []int
	var result []int
	bucket = make([]int, max+1)

	for _, v := range arr {
		bucket[v] += 1
	}

	for j := 0; j < max; j++ {
		if bucket[j] != 0 {
			for y := 0; y < bucket[j]; y++ {
				result = append(result, j)
			}
		}

	}

	fmt.Println(result)
	return result
}
func main() {
	BucketSort([]int{3, 1, 6, 4, 9, 7, 4, 1, 3})
}
