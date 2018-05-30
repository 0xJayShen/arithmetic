package main

import "fmt"

func quickSort( list []int ,start int,end int){
	if start < end{
		i,j := start,end
		key := list[(start+end)/2]
		for i <= j{
			for list[i] < key{
				i++
			}
			for list[j] > key{
				j--
			}
			if i <=j{
				list[i],list[j] = list[j],list[i]
				i++
				j--
			}

		}
		if start < j{
			quickSort(list,start,j)
		}
		if end > i{
			quickSort(list,i,end)
		}

	}
}

func main(){
	list := []int{3,45,34,134,67,6,7657465,33}
	start := 0
	end := len(list)-1
	quickSort(list,start,end)
	fmt.Println(list)
}
