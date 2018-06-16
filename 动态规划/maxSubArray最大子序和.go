package main

func maxSubArray(nums []int)int{
	max_sum := nums[0]
	pre_num := 0
	for _,num := range nums{
		if pre_num > 0{
			pre_num  = pre_num + num
		}else {
			pre_num = num
		}
		if pre_num > max_sum{
			max_sum = pre_num
		}
	}
	return max_sum
}