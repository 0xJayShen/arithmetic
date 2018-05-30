package main

import (
	"fmt"
)

//func add1(num int) (result int) {
//	for i := 1; i <= num; i++ {
//		result = result + i
//	}
//	fmt.Println(result)
//	return result
//}
//
//func main(){
//	add1(3)
//}
//
//func add2(num int)(result int){
//	if num ==1 {
//		result =1
//		return result
//	}else {
//		result = num + add2(num-1)
//		fmt.Println(result)
//		return result
//	}
//}
//func main()  {
//	add2(3)
//}

func hanoi(n int,a,b,c string){
	if n ==1{
		fmt.Println(n,"from",a , "to", c)
	}else{
		hanoi(n-1,a,c,b)
		fmt.Println(n,"from", a ,"to" ,c)
		hanoi(n-1,b,a,c)
	}
}
func main(){
	hanoi(5,"A","B","C")
}