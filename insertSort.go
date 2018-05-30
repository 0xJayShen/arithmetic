package main

import "fmt"

func InsertSort(arr []int){
	var i, j int
	for i=1;i<len(arr);i++{ //控制外循环
		j=i
		for (j > 0&&arr[j]<arr[j-1]){ //内循环
			arr[j-1],arr[j] = arr[j],arr[j-1]
			j--
		}
	}
	fmt.Println(arr)
}



func main(){
	InsertSort([]int{4,5,2,8,3,99})
}