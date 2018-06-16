package 数组题
//https://leetcode-cn.com/problems/two-sum/description/
func twoSum(nums []int, target int) []int {
	m := make(map[int]int ,len(nums))
	for i,value :=range nums{
		if j,ok :=m[target-value];ok{
			// ok 为 true
			// 说明在i之前，存在nums[j] == a
			return []int{j, i}
		}
		//{2:1,3:2,11:3,15:4}
		m[nums[i]] = i
	}
	return nil
}
