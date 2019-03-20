# -*- coding: utf8 -*-
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    for i in range(1, length):
        # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
        subMaxSum = max(nums[i] + nums[i - 1], nums[i])
        nums[i] = subMaxSum  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
    print(max(nums))
    return max(nums)

maxSubArray([13,4,5,6,2,45,6,67])