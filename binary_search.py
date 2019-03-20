# -*- coding: utf8 -*-
def binary_search(my_list, target):
    low = 0
    height = len(my_list) - 1
    while low <= height:
        mid = (low + height) // 2
        guess = my_list[mid]
        if guess > target:
            height = mid - 1
        elif guess < target:
            low = mid + 1
        else:
            print(mid)
            return mid
    return None
binary_search([1,3,5,8,20,],8)


