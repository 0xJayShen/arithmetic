package 回溯法

import "fmt"

func dfs(i int, list []int, res [][]int, part []int) [][]int {

	res = append(res, part)
	fmt.Println("这是 res",res)
	fmt.Println("这是 part",part)
	
	for j := i; j < len(list); j++ {
		res = dfs(j+1, list, res, append(part, list[j]))
	}

	return res
}
func Backtrack(list []int) [][]int {
	var res [][]int
	var part []int
	res = dfs(0, list, res, part)
	fmt.Println(res)
	return res
}

//func dfs(i int ,list[]int,res *[][]int ,part []int)[][]int{
//	*res = append(*res,part)
//
//	for j:=i;j<len(list);j++   {
//		dfs(j+1,list,res,append(part,list[j]))
//	}
//
//	return *res
//}
//
//
//func Backtrack(list []int)[][]int{
//	var res [][]int
//	var part []int
//	res = dfs(0,list,&res,part)
//	fmt.Println(res)
//	return res
//}

func main() {
	Backtrack([]int{1, 2, 3})
}
