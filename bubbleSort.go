package main

import "fmt"

func bubble(myList []int) []int {
	myListLength := len(myList)
	for i := 0; i < myListLength; i++ {
		for j := 0; j < myListLength; j++ {
			if myList[i]< myList[j]{
				myList[j],myList[i] = myList[i],myList[j]
			}
		}
	}
	fmt.Println(myList)
	return myList
}

func main() {
bubble([]int{3,56,324,56,562,2123,1})
}
