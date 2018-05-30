package main

import "fmt"

func SelectSort(list []int){
	l := len(list)
	m := len(list) -1
	for i:=0;i<m;i++{
		tem := i
		for j:=i+1;j<l;j++{
			if list[j] < list[tem]{
				tem = j
			}
		}
		if tem != i{
			list[tem],list[i] = list[i],list[tem]
		}

	}
	fmt.Println(list)
}

func main(){
	SelectSort([]int{3,4,1,5,345,13,1,6})
}
