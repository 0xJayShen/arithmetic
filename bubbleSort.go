package main

import "fmt"

func bubbleSort(my_list []int) []int{
	fmt.Println(my_list)
	for i:=0;i<len(my_list);i++{
		for j:=i+1;j<len(my_list);j++{
			if my_list[i]>my_list[j]{
				my_list[i],my_list[j] = my_list[j],my_list[i]
			}
		}
	}
	fmt.Println(my_list)
	return my_list
}

func main(){
	bubbleSort([]int{3,56,324,56,562,2123,1})
}
