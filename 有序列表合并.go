package main

import "fmt"

func merge(list1, list2 []int) {
	resList := []int{}
	list1Point := 0
	list2Point := 0
	list1Length := len(list1)
	list2Length := len(list2)
	for {
		if list1Point == list1Length {
			resList = append(resList, list2[list2Point:list2Length]...)
			break
		}
		if list1Point == list2Length {
			resList = append(resList, list1[list1Point:list1Length]...)
			break
		}
		list1Num := list1[list1Point]
		list2Num := list2[list2Point]
		if list1Num <= list2Num {
			resList = append(resList, list1Num)
			list1Point++
		} else {
			resList = append(resList, list2Num)
			list2Point++
		}
	}
	fmt.Println(resList)
}
func main() {
	merge([]int{3, 5, 7, 9}, []int{1, 2, 8, 12})
}
