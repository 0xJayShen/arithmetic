package main

import "fmt"

//func example(prices []int)int{
//	var res int
//	for i:= 0;i<len(prices);i++{
//		for j:=i+1;j<len(prices);j++{
//			if prices[j]-prices[i] > res{
//				res = prices[j]-prices[i]
//			}
//		}
//	}
//	fmt.Println(res)
//	return res
//}
//
//func main(){
//	example([]int{1,3,10,4,9})
//}
func dynamic(prices []int) int {
	begin_value := prices[0]
	res := 0
	for _, v := range prices {
		if v-begin_value > res {
			res = v - begin_value
		}
		if v < begin_value {
			begin_value = v
		}
	}
	fmt.Println(res)
	return res
}

func main(){
	dynamic([]int{0,1,4,10,5})
}
