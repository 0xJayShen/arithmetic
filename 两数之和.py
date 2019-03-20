# -*- coding: utf8 -*-
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    # 创建一个空字典
    d = {}
    for x in range(n):
        a = target - nums[x]
        # 字典d中存在nums[x]时
        if nums[x] in d:
            return d[nums[x]], x
        # 否则往字典增加键/值对
        else:
            d[a] = x


nums = [2, 11, 15, 7, ]

target = 9
a, b = twoSum(nums, target)
print(a, b)
